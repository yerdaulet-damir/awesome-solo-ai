# Publishing the frontend guide

Edit `guides/cinematic-frontend-not-slop.md` for the article and the root `llms.txt` for the catalog. The existing guide path is retained so older GitHub links continue to work.

Generate the companion website files with Python 3 and an authenticated GitHub CLI:

```bash
python3 scripts/build-frontend-guide.py
python3 scripts/build-frontend-guide.py --check
```

The script uses GitHub's Markdown renderer, then writes a complete static HTML page at `docs/frontend-design/index.html`, a Markdown version with absolute repository links at `docs/frontend-design.md` and the machine-readable catalog at `docs/llms.txt`. It does not fetch or execute code from the resources listed in the guide.

Commit the source and generated files together. The repository's existing GitHub Pages configuration publishes `main:/docs`; no new runtime or server is required. `--check` runs locally without a network request and fails when the source, renderer or published copies have changed without regeneration.

The HTML page links to its canonical URL, Markdown source and related indexes. Its content and section navigation do not require JavaScript. Keep new guide links in the root README, guides/tools/skills indexes, website homepage, machine-readable catalog and sitemap as appropriate.
