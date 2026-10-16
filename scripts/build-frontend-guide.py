import argparse
import hashlib
import html
import json
import posixpath
import re
import subprocess
from datetime import datetime
from pathlib import Path
from string import Template
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'guides/cinematic-frontend-not-slop.md'
OUTPUT = ROOT / 'docs/frontend-design/index.html'
CANONICAL = 'https://yerdaulet-damir.github.io/awesome-solo-ai/frontend-design/'
REPOSITORY = 'https://github.com/yerdaulet-damir/awesome-solo-ai'
DESCRIPTION = 'Curated frontend design resources: GSAP, Motion, 21st.dev, component libraries, inspiration sites and skills for distinctive websites without AI slop.'


def slug(text):
    plain = html.unescape(re.sub(r'<[^>]+>', '', text)).lower()
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', plain))


def absolute_target(target):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or target.startswith('#'):
        return target
    if target.startswith('/'):
        return 'https://github.com' + target
    path = posixpath.normpath(posixpath.join('guides', parts.path))
    resolved = f'{REPOSITORY}/blob/main/{path}'
    if parts.fragment:
        resolved += '#' + parts.fragment
    return resolved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    markdown = SOURCE.read_text()
    published_markdown = re.sub(r'\]\(([^\s)]+)\)', lambda match: '](' + absolute_target(match.group(1)) + ')', markdown)
    digest = hashlib.sha256(SOURCE.read_bytes() + Path(__file__).read_bytes()).hexdigest()
    marker = f'content="{digest}"'
    plain_output = ROOT / 'docs/frontend-design.md'
    machine_output = ROOT / 'docs/llms.txt'
    if args.check:
        checks = [
            OUTPUT.exists() and marker in OUTPUT.read_text(),
            plain_output.exists() and plain_output.read_text() == published_markdown,
            machine_output.exists() and machine_output.read_bytes() == (ROOT / 'llms.txt').read_bytes(),
        ]
        if not all(checks):
            raise SystemExit('Published guide files are stale. Run python3 scripts/build-frontend-guide.py.')
        print('Published HTML, Markdown and llms.txt match their sources.')
        return

    title = markdown.splitlines()[0].removeprefix('# ')
    date_match = re.search(r'^Updated (\d{1,2} [A-Za-z]+ \d{4})\.', markdown, re.M)
    if not date_match:
        raise SystemExit('Guide needs an Updated day month year. line.')
    date_modified = datetime.strptime(date_match.group(1), '%d %B %Y').date().isoformat()
    body_markdown = markdown.split('\n', 1)[1]
    body_markdown = re.sub(r'(?ms)^## Browse this guide\n.*?(?=^## )', '', body_markdown)
    payload = json.dumps({'text': body_markdown, 'mode': 'gfm', 'context': 'yerdaulet-damir/awesome-solo-ai'})
    rendered = subprocess.run(
        ['gh', 'api', 'markdown', '--input', '-'],
        input=payload, text=True, capture_output=True, check=True,
    ).stdout
    headings = []

    def heading(match):
        level, content = match.group(1), match.group(2)
        identifier = slug(content)
        if level == '2':
            label = html.escape(html.unescape(re.sub(r'<[^>]+>', '', content)))
            headings.append(f'<li><a href="#{identifier}">{label}</a></li>')
        return f'<h{level} id="{identifier}">{content}</h{level}>'

    rendered = re.sub(r'<h([23])[^>]*>(.*?)</h\1>', heading, rendered, flags=re.S)

    def link(match):
        target = html.unescape(match.group(1))
        resolved = absolute_target(target)
        return f'href="{html.escape(resolved, quote=True)}"'

    rendered = re.sub(r'href="([^"]+)"', link, rendered)
    def table(match):
        content = match.group(0)
        columns = [html.unescape(re.sub(r'<[^>]+>', '', label)) for label in re.findall(r'<th\b[^>]*>(.*?)</th>', content, flags=re.S)]
        position = 0

        def cell(cell_match):
            nonlocal position
            label = html.escape(columns[position % len(columns)], quote=True)
            position += 1
            return f'<td{cell_match.group(1)} data-label="{label}">{cell_match.group(2)}</td>'

        content = re.sub(r'<td\b([^>]*)>(.*?)</td>', cell, content, flags=re.S)
        return '<div class="table-scroll" tabindex="0" role="region" aria-label="Resource comparison">' + content + '</div>'

    rendered = re.sub(r'<table\b[^>]*>.*?</table>', table, rendered, flags=re.S)
    schema = {
        '@context': 'https://schema.org', '@type': 'Article',
        'headline': title, 'description': DESCRIPTION, 'url': CANONICAL,
        'mainEntityOfPage': CANONICAL, 'inLanguage': 'en', 'dateModified': date_modified,
        'author': {'@type': 'Person', 'name': 'Yerdaulet Damir', 'url': 'https://yerdaulet.xyz'},
        'isPartOf': {'@type': 'WebSite', 'name': 'Awesome Solo AI', 'url': CANONICAL.removesuffix('frontend-design/')},
    }
    template = Template('''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title | Awesome Solo AI</title>
<meta name="description" content="$description">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="source-sha256" content="$digest">
<link rel="canonical" href="$canonical">
<link rel="alternate" type="text/markdown" href="../frontend-design.md" title="Read as Markdown">
<link rel="stylesheet" href="../guide.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&amp;family=Source+Sans+3:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<meta property="og:type" content="article">
<meta property="og:title" content="$title">
<meta property="og:description" content="$description">
<meta property="og:url" content="$canonical">
<meta property="og:site_name" content="Awesome Solo AI">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="$title">
<meta name="twitter:description" content="$description">
<script type="application/ld+json">$schema</script>
</head>
<body>
<a class="skip" href="#guide">Skip to guide</a>
<header class="masthead">
  <a class="wordmark" href="../">Awesome Solo AI</a>
  <nav aria-label="Main navigation"><a href="$repository">Full catalog</a><a href="../llms.txt">For agents</a><a href="../frontend-design.md">Markdown</a></nav>
</header>
<div class="page-title"><p class="breadcrumb"><a href="../">Home</a> / Frontend design</p><h1>$title</h1></div>
<div class="reading-layout">
  <aside><nav aria-label="On this page"><div class="desktop-contents"><p class="toc-label">On this page</p><ol>$headings</ol></div><details class="mobile-contents"><summary>Browse guide sections</summary><ol>$headings</ol></details></nav></aside>
  <main id="guide" class="content">$body</main>
</div>
<footer><a href="$source">Edit this guide on GitHub</a><a href="../">Awesome Solo AI</a><a href="../llms.txt">Machine-readable index</a></footer>
</body>
</html>
''')
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(template.substitute(
        title=html.escape(title), description=html.escape(DESCRIPTION, quote=True),
        canonical=CANONICAL, digest=digest, schema=json.dumps(schema).replace('<', '\\u003c'),
        repository=REPOSITORY, source=f'{REPOSITORY}/blob/main/guides/cinematic-frontend-not-slop.md',
        headings=''.join(headings), body=rendered,
    ))
    plain_output.write_text(published_markdown)
    machine_output.write_bytes((ROOT / 'llms.txt').read_bytes())
    print('Built docs/frontend-design/index.html, docs/frontend-design.md and docs/llms.txt.')


if __name__ == '__main__':
    main()
