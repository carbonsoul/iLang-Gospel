#!/usr/bin/env python3
"""Refresh only the marked README catalog from the article files."""
from pathlib import Path
import argparse
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN AUTO ARTICLES -->'
END = '<!-- END AUTO ARTICLES -->'
BOOKS = ('Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|'
         '[123] Samuel|[12] Kings|[12] Chronicles|Ezra|Nehemiah|Esther|Job|'
         'Psalms?|Proverbs|Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|'
         'Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|'
         'Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|'
         'John|Acts|Romans|[12] Corinthians|Galatians|Ephesians|Philippians|'
         'Colossians|[12] Thessalonians|[12] Timothy|Titus|Philemon|Hebrews|'
         'James|[12] Peter|[123] John|Jude|Revelation')
REFERENCE = re.compile(r'\b(?:' + BOOKS + r')\s+\d+(?::\d+(?:[-–]\d+)?)?\b')


def escape_cell(value):
    return value.replace('\\', '\\\\').replace('|', '&#124;').replace('[', '\\[').replace(']', '\\]')


def catalog(root):
    rows = ['| Essay | Scripture |', '| :--- | :--- |']
    for path in sorted((root / 'articles').glob('*.md')):
        content = path.read_text(encoding='utf-8')
        heading = re.search(r'^#\s+(.+?)\s*$', content, re.MULTILINE)
        if not heading:
            raise ValueError(f'{path.name} needs a Markdown H1 title')
        title = heading.group(1).split(' — ', 1)[-1]
        reference = REFERENCE.search(content)
        scripture = reference.group(0) if reference else 'See essay'
        url = quote(path.relative_to(root).as_posix(), safe='/')
        rows.append(f'| [{escape_cell(title)}]({url}) | {scripture} |')
    return '\n'.join(rows)


def render_readme(root):
    text = (root / 'README.md').read_text(encoding='utf-8')
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('README must contain exactly one pair of catalog markers')
    before, rest = text.split(START)
    _, after = rest.split(END)
    return before + START + '\n' + catalog(root) + '\n' + END + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    generated = render_readme(ROOT)
    readme = ROOT / 'README.md'
    if args.check:
        if generated != readme.read_text(encoding='utf-8'):
            parser.exit(1, 'README article catalog needs synchronization\n')
    else:
        readme.write_text(generated, encoding='utf-8')
    print('README catalog is synchronized')


if __name__ == '__main__':
    main()
