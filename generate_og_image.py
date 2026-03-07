"""
Generate a branded 1200x630 Open Graph image for MFM Presentations.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PATH = "landing-page/public/og-image.png"
WIDTH, HEIGHT = 1200, 630

# Brand colors (matching the site's dark theme)
BG_COLOR       = (7, 17, 28)       # --bg: #07111c
PANEL_COLOR    = (11, 28, 44)      # --panel: #0b1c2c
ACCENT_COLOR   = (53, 208, 255)    # --accent: #35d0ff
ACCENT2_COLOR  = (255, 77, 109)    # --accent2: #ff4d6d
FG_COLOR       = (244, 247, 251)   # --fg: #f4f7fb
MUTED_COLOR    = (183, 196, 214)   # --muted: #b7c4d6
LINE_COLOR     = (22, 50, 74)      # --line: #16324a

img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Background panel (subtle inner rect)
draw.rectangle([40, 40, WIDTH - 40, HEIGHT - 40], fill=PANEL_COLOR, outline=LINE_COLOR, width=2)

# Accent top bar
draw.rectangle([40, 40, WIDTH - 40, 48], fill=ACCENT_COLOR)

# Accent bottom bar
draw.rectangle([40, HEIGHT - 48, WIDTH - 40, HEIGHT - 40], fill=ACCENT_COLOR)

# Load fonts — fall back to default if system fonts unavailable
def load_font(size):
    for font_name in [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]:
        try:
            return ImageFont.truetype(font_name, size)
        except (IOError, OSError):
            continue
    return ImageFont.load_default()

font_large  = load_font(72)
font_medium = load_font(36)
font_small  = load_font(26)
font_tag    = load_font(22)

# "MFM" in accent color + "Presentations" in white
draw.text((100, 110), "MFM", font=font_large, fill=ACCENT_COLOR)
mfm_bbox = draw.textbbox((0, 0), "MFM", font=font_large)
mfm_w = mfm_bbox[2] - mfm_bbox[0]
draw.text((100 + mfm_w + 20, 110), "Presentations", font=font_large, fill=FG_COLOR)

# Tagline
tagline = "Open-Source Maternal-Fetal Medicine Education"
draw.text((100, 210), tagline, font=font_medium, fill=MUTED_COLOR)

# Divider line
draw.rectangle([100, 270, WIDTH - 100, 274], fill=LINE_COLOR)

# Subtitle
draw.text((100, 298), "Evidence-based clinical presentations and interactive tools", font=font_small, fill=MUTED_COLOR)
draw.text((100, 336), "for patients, providers, and sonographers.", font=font_small, fill=MUTED_COLOR)

# Stats row
stats = [("80+", "Presentations"), ("6", "Interactive Tools"), ("100%", "Open-Source"), ("Free", "Always")]
stat_x = 100
stat_y = 420
for value, label in stats:
    draw.text((stat_x, stat_y), value, font=font_medium, fill=ACCENT_COLOR)
    v_bbox = draw.textbbox((0, 0), value, font=font_medium)
    draw.text((stat_x, stat_y + 46), label, font=font_tag, fill=MUTED_COLOR)
    stat_x += 230

# URL
url_text = "mfm-presentations.vercel.app"
draw.text((100, 535), url_text, font=font_small, fill=ACCENT_COLOR)

# Author
author_text = "Dr. Chukwuma Onyeije, MFM Specialist"
author_bbox = draw.textbbox((0, 0), author_text, font=font_tag)
author_w = author_bbox[2] - author_bbox[0]
draw.text((WIDTH - 100 - author_w, 535), author_text, font=font_tag, fill=MUTED_COLOR)

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
img.save(OUTPUT_PATH, "PNG", optimize=True)
print(f"Generated {OUTPUT_PATH} ({WIDTH}x{HEIGHT}px, {os.path.getsize(OUTPUT_PATH):,} bytes)")
