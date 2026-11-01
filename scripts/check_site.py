#!/usr/bin/env python3
"""Validate the built site's crawlable pages, internal links and SEO metadata."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import struct
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

BASE = 'https://carbonsoul.github.io/iLang-Gospel'


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.meta = {}
        self.links = []
        self.ids = []
        self.h1s = 0
        self.jsonld = []
        self.in_json = False
        self.in_title = False
        self.title = ''
        self.json_buffer = ''
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1s += 1
        if tag == 'meta':
            self.meta[attrs.get('name', attrs.get('property'))] = attrs.get('content', '')
        if tag in ('a', 'link', 'img'):
            self.links.append((tag, attrs))
        if tag == 'title':
            self.in_title = True
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.in_json = True
            self.json_buffer = ''

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'script' and self.in_json:
            self.jsonld.append(json.loads(self.json_buffer))
            self.in_json = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_json:
            self.json_buffer += data


def validate(site, source):
    expected = sorted(p.stem + '.html' for p in (source / 'articles').glob('*.md'))
    actual = sorted(p.name for p in (site / 'articles').glob('*.html'))
    assert actual == expected, 'Article output differs from source inventory'
    assert not list(site.rglob('*.md')), 'Duplicate raw Markdown output'
    pages = {p.relative_to(site).as_posix(): Page(p.read_text()) for p in site.rglob('*.html')}
    titles, descriptions = [], []
    for path, page in pages.items():
        assert page.title.strip(), path
        assert page.h1s == 1, (path, 'exactly one H1 required', page.h1s)
        assert len(page.ids) == len(set(page.ids)), (path, 'duplicate IDs')
        if path == '404.html':
            assert page.meta.get('robots') == 'noindex'
            continue
        canonical = [a['href'] for t, a in page.links if t == 'link' and a.get('rel') == 'canonical']
        url = BASE + ('/' if path == 'index.html' else '/' + path)
        assert canonical == [url], (path, canonical)
        assert page.meta.get('description'), path
        assert page.meta.get('og:url') == url, path
        assert page.meta.get('twitter:card') == 'summary_large_image', path
        assert page.meta.get('og:image') == BASE + '/assets/social-card.png', path
        assert page.jsonld, path
        if path.startswith('articles/'):
            titles.append(page.title)
            descriptions.append(page.meta['description'])
            assert {j['@type'] for j in page.jsonld} == {'Article', 'BreadcrumbList'}, path
            assert page.jsonld[0]['url'] == url
        for tag, attrs in page.links:
            href = attrs.get('href', attrs.get('src', ''))
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                if not href.startswith(BASE + '/'):
                    continue
            if parsed.path.startswith('/iLang-Gospel/'):
                local = unquote(parsed.path[len('/iLang-Gospel/'):]) or 'index.html'
            elif not parsed.path:
                local = path
            elif not parsed.path.startswith('/'):
                local = (Path(path).parent / unquote(parsed.path)).as_posix()
            else:
                raise AssertionError((path, 'link escapes project base', href))
            target = site / local
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), (path, 'missing local target', href)
            if parsed.fragment and local in pages:
                assert unquote(parsed.fragment) in pages[local].ids, (path, 'missing anchor', href)
    assert len(titles) == len(set(titles)), 'Duplicate article SEO titles'
    assert len(descriptions) == len(set(descriptions)), 'Duplicate article descriptions'
    sitemap = ET.parse(site / 'sitemap.xml')
    locations = [e.text for e in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    for name in expected:
        assert BASE + '/articles/' + name in locations, name
        assert any(a.get('href') == '/iLang-Gospel/articles/' + name for t, a in pages['index.html'].links if t == 'a'), name
    assert all('404.html' not in url and 'DESIGN' not in url and 'README' not in url for url in locations)
    feed = ET.parse(site / 'feed.xml')
    items = feed.findall('./channel/item')
    assert len(items) == len(expected)
    assert {item.findtext('link') for item in items} == {BASE + '/articles/' + name for name in expected}
    image = (site / 'assets/social-card.png').read_bytes()
    assert image[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', image[16:24]) == (1200, 630)
    assert BASE + '/sitemap.xml' in (site / 'robots.txt').read_text()
    print(f'PASS: {len(expected)} articles; crawlable index; unique SEO; JSON-LD; canonical/links; RSS/sitemap; social image')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    validate(args.site, args.source)
