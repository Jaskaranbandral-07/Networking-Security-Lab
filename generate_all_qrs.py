import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

BASE_URL = "https://github.com/Jaskaranbandral-07/Networking-Security-Lab"
OUTPUT_DIR = r"c:\Users\Jaskaran Bandral\Downloads\Networking-Security-Lab-main\Networking-Security-Lab-main\qr-codes"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Color themes per experiment — (qr_color, accent, bg_gradient_top, bg_gradient_bottom)
THEMES = {
    "NS":  ("#1a1a2e", "#00e5ff", "#16213e", "#0f3460"),   # Main (Cyan/Indigo)
    "E1":  ("#0d1117", "#58a6ff", "#0d1117", "#161b22"),   # Exp 1 (Sapphire Blue)
    "E2":  ("#0a2e18", "#00e676", "#0a2e18", "#1b5e20"),   # Exp 2 (Emerald Green)
    "E3":  ("#2e2000", "#ffb300", "#2e2000", "#4e342e"),   # Exp 3 (Amber/Gold)
    "E4":  ("#1a0a2e", "#bb86fc", "#1a0a2e", "#311b92"),   # Exp 4 (PKI Purple)
    "E5":  ("#002e2c", "#00e5ff", "#002e2c", "#004d40"),   # Exp 5 (TLS Teal)
    "E6":  ("#2e0a0a", "#ff5252", "#2e0a0a", "#4a121a"),   # Exp 6 (SSH Crimson)
}

entries = [
    ("NS", "Main Repo",               "",                                                    "qr-main-repo"),
    ("E1", "Classical Ciphers",       "/tree/main/Experiment-1-Classical-Ciphers",            "qr-experiment-1"),
    ("E2", "Cryptographic Hashing",   "/tree/main/Experiment-2-Cryptographic-Hashing-SHA256", "qr-experiment-2"),
    ("E3", "Auth & Replay Defense",   "/tree/main/Experiment-3-Authentication-Replay-Defense", "qr-experiment-3"),
    ("E4", "PKI & X.509 Certs",       "/tree/main/Experiment-4-PKI-X509-Certificates",        "qr-experiment-4"),
    ("E5", "TLS Handshake",           "/tree/main/Experiment-5-TLS-Handshake-Analysis",       "qr-experiment-5"),
    ("E6", "SSH Protocol Analysis",   "/tree/main/Experiment-6-SSH-Protocol-Analysis",        "qr-experiment-6"),
]


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def make_gradient(w, h, top_color, bottom_color):
    """Create a vertical gradient image."""
    img = Image.new("RGB", (w, h))
    t = hex_to_rgb(top_color)
    b = hex_to_rgb(bottom_color)
    for y in range(h):
        ratio = y / max(h - 1, 1)
        r = int(t[0] + (b[0] - t[0]) * ratio)
        g = int(t[1] + (b[1] - t[1]) * ratio)
        bl = int(t[2] + (b[2] - t[2]) * ratio)
        ImageDraw.Draw(img).line([(0, y), (w, y)], fill=(r, g, bl))
    return img


def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle."""
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def make_center_badge(text, size, accent_color):
    """Create a circular badge with the experiment number/initials."""
    badge = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(badge)

    # Outer circle — accent color
    d.ellipse([0, 0, size - 1, size - 1], fill=accent_color)

    # Inner circle — dark
    inner_margin = int(size * 0.12)
    d.ellipse(
        [inner_margin, inner_margin, size - 1 - inner_margin, size - 1 - inner_margin],
        fill="#0d1117",
    )

    # Inner ring — subtle accent
    ring_margin = int(size * 0.18)
    d.ellipse(
        [ring_margin, ring_margin, size - 1 - ring_margin, size - 1 - ring_margin],
        fill=None,
        outline=accent_color,
        width=2,
    )

    # Text
    try:
        font_size = int(size * 0.38) if len(text) <= 2 else int(size * 0.28)
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()

    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (size - tw) // 2
    ty = (size - th) // 2 - bbox[1]
    d.text((tx, ty), text, fill="white", font=font)

    return badge


def make_qr(key, label, url, filename):
    theme = THEMES[key]
    qr_color, accent, bg_top, bg_bot = theme

    # Generate QR with high error correction
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="white", back_color=(0, 0, 0, 0))
    qr_img = qr_img.convert("RGBA")
    qr_w, qr_h = qr_img.size

    # Create center badge
    badge_size = int(qr_w * 0.22)
    badge = make_center_badge(key, badge_size, accent)

    bx = (qr_w - badge_size) // 2
    by = (qr_h - badge_size) // 2
    qr_img.paste(badge, (bx, by), badge)

    # Build card
    padding = 48
    top_area = 70
    bottom_area = 55
    card_w = qr_w + padding * 2
    card_h = top_area + qr_h + bottom_area + padding

    card = make_gradient(card_w, card_h, bg_top, bg_bot)
    draw = ImageDraw.Draw(card)

    draw_rounded_rect(draw, [3, 3, card_w - 4, card_h - 4], radius=24, fill=None, outline=accent, width=2)

    qr_rgb = Image.new("RGB", qr_img.size, hex_to_rgb(bg_bot))
    qr_rgb.paste(qr_img, mask=qr_img.split()[3])
    card.paste(qr_rgb, (padding, top_area))

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 22)
        font_sub = ImageFont.truetype("arial.ttf", 13)
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    full_label = f"Experiment {key[1]}: {label}" if key.startswith("E") else "Network Security Lab — Main"
    bbox = draw.textbbox((0, 0), full_label, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((card_w - tw) / 2, 22), full_label, fill="white", font=font_title)

    scan_text = "Scan to view on GitHub"
    bbox2 = draw.textbbox((0, 0), scan_text, font=font_sub)
    tw2 = bbox2[2] - bbox2[0]
    yt = top_area + qr_h + 16
    draw.text(((card_w - tw2) / 2, yt), scan_text, fill=accent, font=font_sub)

    dot_r = 4
    margin = 18
    for cx, cy in [(margin, margin), (card_w - margin, margin),
                   (margin, card_h - margin), (card_w - margin, card_h - margin)]:
        draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=accent)

    out_path = os.path.join(OUTPUT_DIR, f"{filename}.png")
    card.save(out_path, "PNG")
    print(f"  ✅ {filename}.png")


print("🎨 Generating styled QR codes...\n")
for key, label, suffix, fname in entries:
    url = BASE_URL + suffix
    make_qr(key, label, url, fname)

print(f"\n✅ All individual QR codes saved to: {OUTPUT_DIR}")


# --- NOW GENERATE A4 PRINTABLE SHEET ---
print("\n📄 Generating A4 Printable Single-Sheet (PNG + PDF)...")

A4_W, A4_H = 2480, 3508
MARGIN = 60
BG_COLOR = "white"

qr_files = [
    ("qr-main-repo.png",     "Main Repo"),
    ("qr-experiment-1.png",  "Exp 1: Classical Ciphers"),
    ("qr-experiment-2.png",  "Exp 2: Cryptographic Hashing"),
    ("qr-experiment-3.png",  "Exp 3: Auth & Replay Defense"),
    ("qr-experiment-4.png",  "Exp 4: PKI & X.509 Certs"),
    ("qr-experiment-5.png",  "Exp 5: TLS Handshake"),
    ("qr-experiment-6.png",  "Exp 6: SSH Protocol Analysis"),
]

page = Image.new("RGB", (A4_W, A4_H), BG_COLOR)
draw = ImageDraw.Draw(page)

try:
    font_title = ImageFont.truetype("arialbd.ttf", 64)
    font_sub = ImageFont.truetype("arial.ttf", 32)
    font_footer = ImageFont.truetype("arial.ttf", 26)
except OSError:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_footer = font_title

title = "Networking & Network Security Lab"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((A4_W - tw) / 2, MARGIN - 10), title, fill="#0d1117", font=font_title)

subtitle = "Scan any QR code to open the experiment on GitHub"
bbox2 = draw.textbbox((0, 0), subtitle, font=font_sub)
tw2 = bbox2[2] - bbox2[0]
draw.text(((A4_W - tw2) / 2, MARGIN + 75), subtitle, fill="#656d76", font=font_sub)

y_sep = MARGIN + 130
draw.line([(MARGIN + 60, y_sep), (A4_W - MARGIN - 60, y_sep)], fill="#d0d7de", width=2)

qr_images = []
for fname, label in qr_files:
    path = os.path.join(OUTPUT_DIR, fname)
    img = Image.open(path)
    qr_images.append((img, label))

footer_h = 80
content_top = y_sep + 30
content_bottom = A4_H - footer_h
available_h = content_bottom - content_top

gap = 25
main_h = int(available_h * 0.36)
exp_h = int((available_h - main_h - gap * 2) / 2)

main_img = qr_images[0][0]
main_resized = main_img.resize((main_h, main_h), Image.LANCZOS)
main_x = (A4_W - main_h) // 2
main_y = content_top
page.paste(main_resized, (main_x, main_y))

cols = 3
usable_w = A4_W - 2 * MARGIN
col_gap = 25
cell_size = (usable_w - col_gap * (cols - 1)) // cols
cell_size = min(cell_size, exp_h)

total_row_w = cell_size * cols + col_gap * (cols - 1)
row_x_start = (A4_W - total_row_w) // 2

rows_data = [
    qr_images[1:4],
    qr_images[4:7],
]

for row_idx, row in enumerate(rows_data):
    for col_idx, (img, label) in enumerate(row):
        resized = img.resize((cell_size, cell_size), Image.LANCZOS)
        x = row_x_start + col_idx * (cell_size + col_gap)
        y = content_top + main_h + gap + row_idx * (cell_size + gap)
        page.paste(resized, (x, y))

draw.line([(MARGIN + 60, A4_H - footer_h - 10), (A4_W - MARGIN - 60, A4_H - footer_h - 10)], fill="#d0d7de", width=2)
footer = "github.com/Jaskaranbandral-07/Networking-Security-Lab"
bbox3 = draw.textbbox((0, 0), footer, font=font_footer)
tw3 = bbox3[2] - bbox3[0]
draw.text(((A4_W - tw3) / 2, A4_H - footer_h + 10), footer, fill="#656d76", font=font_footer)

out_png = os.path.join(OUTPUT_DIR, "ALL-QR-CODES-PRINTABLE.png")
page.save(out_png, "PNG", dpi=(300, 300))
print(f"  ✅ PNG saved: {out_png}")

out_pdf = os.path.join(OUTPUT_DIR, "ALL-QR-CODES-PRINTABLE.pdf")
page.save(out_pdf, "PDF", resolution=300)
print(f"  ✅ PDF saved: {out_pdf}")

print("\n🎉 All QR generation complete!")
