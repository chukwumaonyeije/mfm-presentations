"""
inject_deck_seo.py — OpenMFM Per-Deck SEO Injector
====================================================
Reads landing-page/data/presentations.json and injects into every deck HTML file:
  - <link rel="canonical">
  - <meta name="description">
  - Open Graph tags (og:type, og:url, og:title, og:description, og:image, og:site_name)
  - Twitter Card tags
  - <meta name="author"> and <meta name="keywords">
  - JSON-LD structured data using schema.org MedicalWebPage
  - A fixed-position branded "← OpenMFM Library" backlink footer

The script is idempotent: files already injected (marked with SEO_MARKER) are skipped.
Run from the repository root.
"""

import json
import os
import re
import sys
from datetime import datetime
from urllib.parse import unquote

# ── Constants ────────────────────────────────────────────────────────────────
BASE_URL   = "https://openmfm.org"
REPO_ROOT  = os.path.dirname(os.path.abspath(__file__))
JSON_PATH  = os.path.join(REPO_ROOT, "landing-page", "data", "presentations.json")

SEO_MARKER    = "<!-- openmfm-seo-injected -->"
FOOTER_MARKER = "<!-- openmfm-footer-injected -->"

# ── Helpers ──────────────────────────────────────────────────────────────────

def get_description(p):
    """Return the description field, or synthesise one from title + tags."""
    if p.get("description"):
        return p["description"]
    tags = p.get("tags", [])[:3]
    tag_str = ", ".join(tags) if tags else ""
    title   = p["title"]
    suffix  = f" Topics: {tag_str}." if tag_str else ""
    return f"Evidence-based MFM education on {title} by Dr. Chukwuma Onyeije, MD.{suffix}"


def esc_attr(s):
    """Escape double-quotes and angle brackets for use inside HTML attributes."""
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def build_seo_block(title, description, canonical_url, keywords, today):
    ld = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": title,
        "description": description,
        "url": canonical_url,
        "author": {
            "@type": "Person",
            "name": "Dr. Chukwuma Onyeije, MD",
            "jobTitle": "Maternal-Fetal Medicine Specialist",
            "worksFor": {
                "@type": "Organization",
                "name": "Atlanta Perinatal Associates"
            }
        },
        "publisher": {
            "@type": "Organization",
            "name": "OpenMFM",
            "url": "https://openmfm.org",
            "logo": {
                "@type": "ImageObject",
                "url": "https://openmfm.org/og-image.png"
            }
        },
        "dateModified": today,
        "inLanguage": "en",
        "audience": {
            "@type": "MedicalAudience",
            "audienceType": "Patients and Healthcare Providers"
        },
        "about": {
            "@type": "MedicalCondition",
            "name": title
        },
        "isPartOf": {
            "@type": "WebSite",
            "name": "OpenMFM",
            "url": "https://openmfm.org"
        },
        "keywords": keywords
    }

    ld_str   = json.dumps(ld, indent=2, ensure_ascii=False)
    e_title  = esc_attr(title)
    e_desc   = esc_attr(description)

    return f"""{SEO_MARKER}
<link rel="canonical" href="{canonical_url}">
<meta name="description" content="{e_desc}">
<meta name="author" content="Dr. Chukwuma Onyeije, MD">
<meta name="keywords" content="{esc_attr(keywords)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical_url}">
<meta property="og:title" content="{e_title} | OpenMFM">
<meta property="og:description" content="{e_desc}">
<meta property="og:image" content="https://openmfm.org/og-image.png">
<meta property="og:site_name" content="OpenMFM">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e_title} | OpenMFM">
<meta name="twitter:description" content="{e_desc}">
<meta name="twitter:image" content="https://openmfm.org/og-image.png">
<script type="application/ld+json">
{ld_str}
</script>"""


FOOTER_HTML = f"""{FOOTER_MARKER}
<div style="position:fixed;bottom:16px;left:16px;z-index:9999;background:rgba(15,23,42,0.88);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);border:1px solid rgba(34,211,238,0.35);border-radius:8px;padding:5px 14px;font-family:system-ui,-apple-system,sans-serif;pointer-events:auto;">
  <a href="https://openmfm.org/library" style="color:#22d3ee;text-decoration:none;font-size:12px;font-weight:500;letter-spacing:0.02em;white-space:nowrap;">&#8592; OpenMFM Library</a>
</div>"""


# ── Strip helper (used by --force) ───────────────────────────────────────────

def strip_injected_blocks(content):
    """Remove previously injected SEO and footer blocks so they can be re-injected."""
    # SEO block: from marker to the closing </script> of the JSON-LD
    content = re.sub(
        r'<!-- openmfm-seo-injected -->.*?</script>',
        '',
        content,
        flags=re.DOTALL,
    )
    # Footer block: from marker to its closing </div>
    content = re.sub(
        r'<!-- openmfm-footer-injected -->.*?</div>',
        '',
        content,
        flags=re.DOTALL,
    )
    return content


# ── Core injection ───────────────────────────────────────────────────────────

def inject_presentation(p, today, force=False):
    href  = p["href"]
    title = p["title"]

    # Build canonical URL using the href as-is (preserving any %20 etc.)
    canonical_url = f"{BASE_URL}/{href}"

    # Resolve actual file path: URL-decode then use OS path separator
    file_rel  = unquote(href).replace("/", os.sep)
    file_path = os.path.join(REPO_ROOT, file_rel)

    if not os.path.exists(file_path):
        print(f"  ⚠  NOT FOUND : {file_rel}")
        return False

    with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
        content = fh.read()

    # ── Idempotency / force ────────────────────────────────────────────────
    if SEO_MARKER in content:
        if not force:
            print(f"  ✓  Skipped   : {href}")
            return True
        # force=True: strip old blocks and re-inject with updated description
        content = strip_injected_blocks(content)
        print(f"  🔄 Updating  : {href}")

    description = get_description(p)
    keywords    = ", ".join(p.get("tags", []))
    seo_block   = build_seo_block(title, description, canonical_url, keywords, today)

    # ── Strip any existing bare <meta name="description"> to avoid duplicates ──
    content = re.sub(
        r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']\s*/?>',
        "",
        content,
        flags=re.IGNORECASE,
    )

    # ── Inject SEO block just before </head> ──────────────────────────────
    if "</head>" in content:
        content = content.replace("</head>", f"{seo_block}\n</head>", 1)
    else:
        # Fallback: prepend to file
        content = seo_block + "\n" + content

    # ── Inject footer before </body> ──────────────────────────────────────
    if FOOTER_MARKER not in content:
        if "</body>" in content:
            content = content.replace("</body>", f"{FOOTER_HTML}\n</body>", 1)
        else:
            content += "\n" + FOOTER_HTML

    with open(file_path, "w", encoding="utf-8") as fh:
        fh.write(content)

    print(f"  ✅ Injected  : {href}")
    return True


# ── Entry point ──────────────────────────────────────────────────────────────

def main():
    force = "--force" in sys.argv

    with open(JSON_PATH, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    presentations = data["presentations"]
    today         = datetime.now().strftime("%Y-%m-%d")

    mode_label = " (FORCE — re-injecting all)" if force else ""
    print(f"\nOpenMFM — inject_deck_seo.py{mode_label}")
    print(f"Processing {len(presentations)} presentations …\n")

    ok  = 0
    err = 0

    for p in presentations:
        result = inject_presentation(p, today, force=force)
        if result:
            ok += 1
        else:
            err += 1

    print(f"\n{'─'*50}")
    print(f"Done.  Injected: {ok}  |  Failed/Not Found: {err}")
    if err:
        print("  → Check the ⚠ lines above and verify href paths in presentations.json.")


if __name__ == "__main__":
    main()
