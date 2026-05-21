from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = "output/pdf/baby-jackpot-thank-you.pdf"
FONT_PATH = "sparkystones.ttf"
ROUND_FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
URL = "https://bigreveal.joyjotstudio.store/create"
PASSWORD = "spintowin1234"

PAGE_W, PAGE_H = letter

PEACH = colors.HexColor("#f28b70")
MUSTARD = colors.HexColor("#dca52a")
TEAL = colors.HexColor("#70b4aa")
CREAM = colors.HexColor("#fcf1de")
PAPER = colors.HexColor("#fffaf0")
INK = colors.HexColor("#23190f")
LINE = colors.HexColor("#e9b868")
GOLD_LIGHT = colors.HexColor("#ffe99a")
GOLD = colors.HexColor("#e3ad2c")
BLUE_GRAY = colors.HexColor("#38577f")


def register_fonts():
    try:
        pdfmetrics.registerFont(TTFont("Sparky", FONT_PATH))
        display = "Sparky"
    except Exception:
        display = "Helvetica-Bold"
    try:
        pdfmetrics.registerFont(TTFont("Rounded", ROUND_FONT_PATH))
        rounded = "Rounded"
    except Exception:
        rounded = "Helvetica-Bold"
    return display, rounded


DISPLAY_FONT, ROUNDED_FONT = register_fonts()


def rounded_rect(c, x, y, w, h, r, fill, stroke=None, sw=1):
    c.setLineWidth(sw)
    c.setFillColor(fill)
    c.setStrokeColor(stroke or fill)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)


def centered_text(c, text, x, y, w, font, size, color, shadow=False):
    if shadow:
        c.setFillColor(colors.Color(0.55, 0.34, 0.22, alpha=0.22))
        c.setFont(font, size)
        c.drawCentredString(x + w / 2 + 1.4, y - 1.8, text)
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawCentredString(x + w / 2, y, text)


def draw_wrapped(c, text, x, y, w, size=18, leading=24, align="CENTER"):
    style = ParagraphStyle(
        "body",
        fontName=ROUNDED_FONT,
        fontSize=size,
        leading=leading,
        textColor=INK,
        alignment={"LEFT": 0, "CENTER": 1}[align],
    )
    p = Paragraph(text, style)
    _, h = p.wrap(w, 500)
    p.drawOn(c, x, y - h)
    return h


def dotted_line(c, x1, y, x2):
    c.setStrokeColor(LINE)
    c.setLineWidth(3.2)
    c.setDash(2.2, 4.2)
    c.line(x1, y, x2, y)
    c.setDash()


def icon_circle(c, cx, cy, kind):
    c.setFillColor(GOLD_LIGHT)
    c.setStrokeColor(colors.Color(0.93, 0.72, 0.25, alpha=0.2))
    c.setLineWidth(1)
    c.circle(cx, cy, 27, fill=1, stroke=1)
    c.setStrokeColor(BLUE_GRAY)
    c.setLineWidth(2.2)
    if kind == "screen":
        c.roundRect(cx - 18, cy - 10, 36, 24, 2, fill=0, stroke=1)
        c.line(cx, cy - 10, cx, cy - 18)
        c.line(cx - 10, cy - 18, cx + 10, cy - 18)
    elif kind == "lock":
        c.roundRect(cx - 14, cy - 15, 28, 22, 3, fill=0, stroke=1)
        c.arc(cx - 13, cy - 2, cx + 13, cy + 24, 0, 180)
        c.line(cx - 13, cy + 11, cx - 13, cy + 4)
        c.line(cx + 13, cy + 11, cx + 13, cy + 4)
        c.circle(cx, cy - 3, 2, fill=1, stroke=1)
        c.line(cx, cy - 5, cx, cy - 11)
    elif kind == "link":
        c.arc(cx - 22, cy - 6, cx + 2, cy + 18, 118, 225)
        c.arc(cx - 2, cy - 18, cx + 22, cy + 6, -62, 225)
        c.line(cx - 4, cy + 5, cx + 7, cy - 6)
    elif kind == "share":
        c.line(cx - 18, cy - 13, cx + 14, cy + 18)
        c.line(cx + 14, cy + 18, cx + 11, cy + 3)
        c.line(cx + 14, cy + 18, cx - 1, cy + 16)


def fit_display_text(c, text, font, max_size, max_w):
    size = max_size
    while size > 10 and stringWidth(text, font, size) > max_w:
        size -= 1
    return size


def step(c, y_top, number, title, icon, lines, pill=None):
    dotted_line(c, 70, y_top, PAGE_W - 70)
    icon_circle(c, 100, y_top - 45, icon)
    title_size = fit_display_text(c, f"{number}. {title}", ROUNDED_FONT, 24, PAGE_W - 180)
    c.setFont(ROUNDED_FONT, title_size)
    c.setFillColor([MUSTARD, TEAL, PEACH, MUSTARD][number - 1])
    c.drawString(155, y_top - 34, f"{number}. {title}")
    text_y = y_top - (65 if pill else 58)
    if pill:
        rounded_rect(c, 242, text_y - 18, 190, 42, 20, GOLD_LIGHT, None)
        centered_text(c, pill, 242, text_y - 5, 190, ROUNDED_FONT, 22, colors.black)
        text_y -= 48
    for line in lines:
        size = 15 if line.startswith("Go to https://") else 17
        c.setFont(ROUNDED_FONT, size)
        c.setFillColor(INK)
        c.drawString(155, text_y, line)
        text_y -= 25


def main():
    c = canvas.Canvas(OUT, pagesize=letter)
    c.setTitle("Baby Jackpot Thank You")

    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    rounded_rect(c, 28, 26, PAGE_W - 56, PAGE_H - 52, 12, PAPER, None)

    centered_text(c, "YOU'RE JUST MOMENTS AWAY", 50, 712, PAGE_W - 100, ROUNDED_FONT, 34, MUSTARD, True)
    centered_text(c, "FROM YOUR CUSTOM REVEAL!", 50, 668, PAGE_W - 100, ROUNDED_FONT, 34, TEAL, True)

    for y, line in [
        (620, "Thanks for your purchase - your interactive digital"),
        (596, "scratch reveal is just a few clicks away! Follow these easy"),
        (572, "steps to personalize and generate your custom link."),
    ]:
        centered_text(c, line, 82, y, PAGE_W - 164, ROUNDED_FONT, 16, INK)

    step(
        c,
        538,
        1,
        "VISIT THE FORM CUSTOMIZER",
        "screen",
        [f"Go to {URL}", "-> You'll be taken to the private reveal link builder."],
    )
    step(
        c,
        420,
        2,
        "ENTER THE PASSWORD",
        "lock",
        ["This will grant access to the form."],
        pill=PASSWORD,
    )
    step(
        c,
        300,
        3,
        "CUSTOMIZE YOUR REVEAL",
        "link",
        ["Fill in the form with your personal touches"],
    )
    step(
        c,
        212,
        4,
        "GENERATE & SHARE YOUR LINK",
        "share",
        ["-> Click Generate URL.", "-> Then click Copy to Clipboard", "-> Paste your link in a text, email, group chat,", "   or share on a social post!"],
    )
    dotted_line(c, 70, 72, PAGE_W - 70)
    centered_text(
        c,
        "If you have any questions at all, do not hesitate to",
        95,
        50,
        PAGE_W - 190,
        ROUNDED_FONT,
        13,
        INK,
    )
    centered_text(
        c,
        "reach out on Etsy! Kristina, Joy Jot Studio",
        95,
        32,
        PAGE_W - 190,
        ROUNDED_FONT,
        13,
        INK,
    )

    c.save()


if __name__ == "__main__":
    main()
