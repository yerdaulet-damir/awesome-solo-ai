import argparse
import hashlib
import html
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'CONTRIBUTING.md'
OUTPUT = ROOT / 'docs/contribute/index.html'
REPOSITORY = 'https://github.com/yerdaulet-damir/awesome-solo-ai'
CANONICAL = 'https://yerdaulet-damir.github.io/awesome-solo-ai/contribute/'


def absolute_target(target):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or target.startswith('#'):
        return target
    if target.startswith('/'):
        return 'https://github.com' + target
    relative = parts.path
    mode = 'tree' if (ROOT / relative).is_dir() else 'blob'
    resolved = f'{REPOSITORY}/{mode}/main/{relative}'
    if parts.fragment:
        resolved += '#' + parts.fragment
    return resolved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    digest = hashlib.sha256(SOURCE.read_bytes() + Path(__file__).read_bytes()).hexdigest()
    if args.check:
        if not OUTPUT.exists() or f'content="{digest}"' not in OUTPUT.read_text():
            raise SystemExit('Contributor page is stale. Run python3 scripts/build-contributor-page.py.')
        print('Contributor page matches its source and renderer.')
        return

    body_markdown = SOURCE.read_text().split('\n', 1)[1]
    payload = json.dumps({'text': body_markdown, 'mode': 'gfm', 'context': 'yerdaulet-damir/awesome-solo-ai'})
    rendered = subprocess.run(
        ['gh', 'api', 'markdown', '--input', '-'],
        input=payload, text=True, capture_output=True, check=True,
    ).stdout
    rendered = re.sub(
        r'href="([^"]+)"',
        lambda match: 'href="' + html.escape(absolute_target(html.unescape(match.group(1))), quote=True) + '"',
        rendered,
    )
    def label_table(match):
        table = match.group(0)
        labels = [html.unescape(re.sub(r'<[^>]+>', '', label)) for label in re.findall(r'<th\b[^>]*>(.*?)</th>', table, flags=re.S)]
        position = 0

        def label_cell(cell):
            nonlocal position
            label = html.escape(labels[position % len(labels)], quote=True)
            position += 1
            return f'<td{cell.group(1)} data-label="{label}">{cell.group(2)}</td>'

        return re.sub(r'<td([^>]*)>(.*?)</td>', label_cell, table, flags=re.S) if labels else table

    rendered = re.sub(r'<table\b[^>]*>.*?</table>', label_table, rendered, flags=re.S)
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contribute AI guides, skills and playbooks | Awesome Solo AI</title>
<meta name="description" content="Publish a practical AI guide, skill or playbook, improve an existing workflow, or recommend a tool you have used. First-time contributors are welcome.">
<meta name="robots" content="index,follow">
<meta name="source-sha256" content="{digest}">
<link rel="canonical" href="{CANONICAL}">
<link rel="alternate" type="text/markdown" href="https://raw.githubusercontent.com/yerdaulet-damir/awesome-solo-ai/main/CONTRIBUTING.md" title="Read as Markdown">
<link rel="stylesheet" href="../guide.css">
</head>
<body>
<a class="skip" href="#contribute">Skip to contribution guide</a>
<header class="masthead"><a class="wordmark" href="../">Awesome Solo AI</a><nav aria-label="Main navigation"><a href="../frontend-design/">Frontend guide</a><a href="../llms.txt">For agents</a><a href="{REPOSITORY}">GitHub</a></nav></header>
<div class="page-title"><p class="breadcrumb"><a href="../">Home</a> / Contribute</p><h1>Contribute a guide, skill or playbook</h1></div>
<div class="reading-layout"><aside><p class="toc-label">Choose a contribution</p><p>First PR? Fix a step you tried or add a worked example to an existing page.</p><p><a href="{REPOSITORY}/issues/new?template=share-a-contribution.yml">Propose an idea</a></p></aside><main id="contribute" class="content">{rendered}</main></div>
<footer><a href="{REPOSITORY}/blob/main/CONTRIBUTING.md">Edit the source guide</a><a href="{REPOSITORY}/tree/main/.github/CONTRIBUTION_TEMPLATES">Contribution templates</a><a href="../">Library</a></footer>
</body>
</html>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(page)
    print('Built docs/contribute/index.html from CONTRIBUTING.md.')


if __name__ == '__main__':
    main()
