"""Build the GitHub Pages files from page.html (the artifact source, which has no <html>/<head>).

Writes index.html (full document with SEO and social tags), robots.txt, sitemap.xml and img/og.jpg.
Run from anywhere: python build.py
"""
import pathlib
import re
from datetime import date

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent
URL = "https://ai.vanssay.net/"
TITLE = "Marin de Vanssay · Cours et ateliers IA pour indépendants, TPE et PME"
DESC = ("Je vous apprends à vous servir de l’IA sur vos vraies tâches, seul ou avec votre équipe, "
        "puis je construis ce qui manque pour que tout tourne dans vos outils.")

page = (ROOT / "page.html").read_text(encoding="utf-8")
# Drop the artifact-only lines; everything else is shared with the artifact preview.
page = re.sub(r"^<title>.*?</title>\s*", "", page, flags=re.M)
page = re.sub(r'^<meta name="claude:viewport-fit-sides"[^>]*>\s*', "", page, flags=re.M)

head = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="apple-touch-icon" href="/favicon-180.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{URL}img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}[hidden]{{display:none!important}}</style>
"""
(ROOT / "index.html").write_text(head + page.replace("<style>", "<style>", 1).replace("\n<header", "</head>\n<body>\n<header", 1) + "\n</body>\n</html>\n", encoding="utf-8")

import cases  # noqa: E402  (case study pages, cas/<slug>.html)
slugs = cases.build()

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL}sitemap.xml\n", encoding="utf-8")
today = date.today().isoformat()
urls = [URL] + [f"{URL}cas/{s}.html" for s in slugs]
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    + "</urlset>\n", encoding="utf-8")
print("case pages:", ", ".join(slugs))

# Social preview: a screenshot of the live hero (img/og-base.jpg, 1200x630) when present,
# otherwise the hero poster with the centered logo drawn on top.
if (ROOT / "img" / "og-base.jpg").exists():
    Image.open(ROOT / "img" / "og-base.jpg").convert("RGB").resize((1200, 630)).save(ROOT / "img" / "og.jpg", quality=86)
    print("built index.html, robots.txt, sitemap.xml, img/og.jpg (from og-base.jpg)")
    raise SystemExit
# Social preview: the hero poster with the centered logo, like the hero itself.
poster = Image.open(ROOT / "img" / "hero-poster.webp").convert("RGB")
w = 1200
poster = poster.resize((w, round(poster.height * w / poster.width)), Image.LANCZOS)
top = (poster.height - 630) // 2
og = poster.crop((0, top, w, top + 630))
glyph = Image.open(ROOT / "img" / "glyph-white.png").convert("RGBA").resize((92, 92), Image.LANCZOS)
font = ImageFont.truetype(r"C:\Windows\Fonts\seguisb.ttf", 112)
small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 34)
d = ImageDraw.Draw(og)
text_w = d.textlength("Vanssay", font=font)
total = 92 + 24 + text_w
x0 = (w - total) / 2
og.paste(glyph, (int(x0), 630 // 2 - 46 - 20), glyph)
d.text((x0 + 92 + 24, 630 // 2 - 20), "Vanssay", font=font, fill=(255, 255, 255), anchor="lm")
d.text((48, 630 - 56), "Cours et ateliers IA pour indépendants, TPE et PME", font=small, fill=(235, 235, 235), anchor="lm")
og.save(ROOT / "img" / "og.jpg", quality=86)
print("built index.html, robots.txt, sitemap.xml, img/og.jpg")
