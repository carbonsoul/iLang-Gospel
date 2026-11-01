import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('sync', Path(__file__).parents[1] / 'scripts/sync_articles.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'articles').mkdir()
        (self.root / 'README.md').write_text('Introduction\n' + sync.START + '\nstale\n' + sync.END + '\nHandwritten footer\n')

    def article(self, name, content):
        (self.root / 'articles' / name).write_text(content)

    def test_add_edit_delete_and_preserve_surroundings(self):
        self.article('020-new.md', '# A new essay\n\nJohn 3:16\n')
        first = sync.render_readme(self.root)
        self.assertTrue(first.startswith('Introduction\n'))
        self.assertTrue(first.endswith('\nHandwritten footer\n'))
        self.assertIn('[A new essay](articles/020-new.md)', first)
        self.article('020-new.md', '# Revised essay\n\nGenesis 1:3\n')
        self.assertIn('[Revised essay]', sync.render_readme(self.root))
        (self.root / 'articles/020-new.md').unlink()
        self.assertNotIn('020-new.md', sync.render_readme(self.root))

    def test_sort_escape_and_numbered_bible_book(self):
        self.article('020-空 格.md', '# A | [test]\n\n1 Samuel 17:33\n')
        self.article('001-start.md', '# First\n\nJohn 1:1\n')
        result = sync.render_readme(self.root)
        self.assertLess(result.index('[First]'), result.index('A &#124;'))
        self.assertIn('1 Samuel 17:33', result)
        self.assertIn('020-%E7%A9%BA%20%E6%A0%BC.md', result)
        self.assertIn('\\[test\\]', result)

    def test_idempotent(self):
        self.article('001-test.md', '# Test\n\nJohn 1:1\n')
        first = sync.render_readme(self.root)
        (self.root / 'README.md').write_text(first)
        self.assertEqual(first, sync.render_readme(self.root))

    def test_missing_title_fails(self):
        self.article('001-test.md', 'No title')
        with self.assertRaises(ValueError):
            sync.render_readme(self.root)

    def test_missing_markers_fails(self):
        (self.root / 'README.md').write_text('Unmarked author text')
        with self.assertRaises(ValueError):
            sync.render_readme(self.root)


if __name__ == '__main__':
    unittest.main()
