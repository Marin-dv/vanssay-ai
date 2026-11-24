# ai.vanssay.net

Marin de Vanssay's one-page site: AI training and automations for small businesses (French first, English later under `/en/`).

- `page.html`: the page itself, without `<html>`/`<head>`. It is also the source of the private Claude artifact preview.
- `build.py`: builds `index.html` (full document with SEO and social tags), `robots.txt`, `sitemap.xml` and `img/og.jpg` from `page.html`. Run `python build.py` after every change to `page.html`, then commit.
- `CNAME`: custom domain for GitHub Pages (ai.vanssay.net). ia.vanssay.net redirects here with a Cloudflare redirect rule.
- Deploy: push to `main` (GitHub Pages serves the repo root).
