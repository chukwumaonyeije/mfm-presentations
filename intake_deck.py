"""
intake_deck.py — import a new deck and register it in OpenMFM
==============================================================

Usage:
  python intake_deck.py "C:\\path\\to\\downloaded.html" --slug alcohol-during-pregnancy

What it does:
  1. Copies the source HTML into decks/<slug>/index.html
  2. Extracts title / description / tags from the source HTML, with optional overrides
  3. Inserts a new card at the top of index.html
  4. Inserts the new presentation at the top of landing-page/data/presentations.json
  5. Injects OpenMFM SEO/footer into the deck HTML

The helper is intentionally conservative:
  - it will not duplicate an existing href in index.html
  - it preserves the existing microsites array in presentations.json
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup

from inject_deck_seo import inject_presentation


REPO_ROOT = Path(__file__).resolve().parent
INDEX_HTML = REPO_ROOT / "index.html"
PRESENTATIONS_JSON = REPO_ROOT / "landing-page" / "data" / "presentations.json"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "new-deck"


def clean_title(raw_title: str, fallback_slug: str) -> str:
    title = html.unescape((raw_title or "").strip())
    if not title:
        return fallback_slug.replace("-", " ").title()

    separators = [
        " | OpenMFM",
        " | MFM Presentations",
        " - OpenMFM",
        " — OpenMFM",
        " - MFM Presentations",
        " — MFM Presentations",
        " - MFM Patient Education",
        " — MFM Patient Education",
    ]
    for suffix in separators:
        if title.endswith(suffix):
            title = title[: -len(suffix)].strip()

    return title


def infer_audience(text: str) -> str | None:
    lowered = text.lower()
    if any(token in lowered for token in ["provider education", "for providers", "provider guide", "clinical management", "journal club"]):
        return "Provider Education"
    if any(token in lowered for token in ["patient education", "expectant parent", "your care team", "what every expectant parent should know", "for patients"]):
        return "Patient Education"
    return None


def extract_metadata(source_path: Path, slug: str) -> tuple[str, str, list[str]]:
    text = source_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(text, "html.parser")

    raw_text = soup.get_text(" ", strip=True)

    title = clean_title(
        (soup.title.string if soup.title and soup.title.string else "")
        or (soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else ""),
        slug,
    )
    audience = infer_audience(raw_text)
    if audience and audience.lower() not in title.lower():
        title = f"{title} - {audience}"

    meta_desc = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    description = ""
    if meta_desc and meta_desc.get("content"):
        description = meta_desc["content"].strip()
    else:
        paragraphs = [
            re.sub(r"\s+", " ", p.get_text(" ", strip=True)).strip()
            for p in soup.find_all("p")
        ]
        candidates = [p for p in paragraphs if len(p) >= 80]
        if candidates:
            description = max(candidates[:12], key=len)
        elif paragraphs:
            description = max(paragraphs[:12], key=len)
    description = re.sub(r"\s+", " ", description).strip()

    meta_keywords = soup.find("meta", attrs={"name": re.compile(r"^keywords$", re.I)})
    tags: list[str] = []
    if meta_keywords and meta_keywords.get("content"):
        tags = [t.strip() for t in meta_keywords["content"].split(",") if t.strip()]

    if not tags:
        core_title = re.sub(r"\s*-\s*(Patient|Provider) Education\s*$", "", title, flags=re.I)
        tags = [core_title]
        if audience:
            tags.append(audience)

    return title, description, tags[:5]


def build_card_html(title: str, description: str, tags: list[str], href: str) -> str:
    escaped_title = html.escape(title)
    escaped_desc = html.escape(description)
    tags_html = "\n".join(f'          <span class="tag">{html.escape(tag)}</span>' for tag in tags)
    return (
        "      <div class=\"card\">\n"
        f"        <h2>{escaped_title}</h2>\n"
        f"        <p>{escaped_desc}</p>\n"
        "        <div>\n"
        f"{tags_html}\n"
        "        </div>\n"
        f"        <a href=\"{href}\" class=\"btn\">View Presentation</a>\n"
        "      </div>\n"
    )


def insert_card_at_top(index_text: str, card_html: str, href: str) -> str:
    if href in index_text:
        raise ValueError(f"{href} is already present in index.html")

    marker = '<div class="presentations">'
    if marker not in index_text:
        raise ValueError("Could not find presentations container in index.html")

    return index_text.replace(marker, marker + "\n" + card_html.rstrip(), 1)


def update_index(title: str, description: str, tags: list[str], href: str) -> None:
    index_text = INDEX_HTML.read_text(encoding="utf-8")
    updated = insert_card_at_top(index_text, build_card_html(title, description, tags, href), href)
    INDEX_HTML.write_text(updated, encoding="utf-8")


def update_presentations_json(title: str, description: str, tags: list[str], href: str) -> None:
    data = json.loads(PRESENTATIONS_JSON.read_text(encoding="utf-8"))
    new_entry = {
        "title": title,
        "href": href,
        "tags": tags,
        "description": description,
    }
    presentations = [p for p in data.get("presentations", []) if p.get("href") != href]
    data["presentations"] = [new_entry, *presentations]
    PRESENTATIONS_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def import_deck(source: Path, slug: str) -> Path:
    deck_dir = REPO_ROOT / "decks" / slug
    deck_dir.mkdir(parents=True, exist_ok=True)
    dest = deck_dir / "index.html"
    shutil.copy2(source, dest)
    return dest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import a downloaded deck and register it in OpenMFM.")
    parser.add_argument("source", help="Path to the downloaded HTML file")
    parser.add_argument("--slug", help="Destination deck slug under /decks")
    parser.add_argument("--title", help="Override parsed deck title")
    parser.add_argument("--description", help="Override parsed description")
    parser.add_argument("--tags", help="Comma-separated tag override list")
    parser.add_argument("--dry-run", action="store_true", help="Validate metadata and destination without writing files")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = Path(args.source)
    if not source.exists():
        raise SystemExit(f"Source file not found: {source}")

    slug = args.slug or slugify(source.stem)
    dest = REPO_ROOT / "decks" / slug / "index.html"

    title, description, tags = extract_metadata(source, slug)
    if args.title:
        title = args.title.strip()
    if args.description:
        description = args.description.strip()
    if args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    href = f"decks/{slug}/index.html"

    if args.dry_run:
        print(f"Would import to {dest}")
        print(f"title: {title}")
        print(f"description: {description}")
        print(f"tags: {tags}")
        print(f"href: {href}")
        return

    dest = import_deck(source, slug)

    update_index(title, description, tags, href)
    update_presentations_json(title, description, tags, href)
    inject_presentation(
        {
            "title": title,
            "href": href,
            "tags": tags,
            "description": description,
        },
        today=__import__("datetime").datetime.now().strftime("%Y-%m-%d"),
        force=True,
    )

    print(f"Imported deck to {dest}")
    print(f"Registered at top of library and presentations data as {href}")


if __name__ == "__main__":
    main()
