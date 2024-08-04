import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extaction(self):
        markdown = "Junk\n\n * ulist\n\n # h1\n\n 1. olist"
        extraction = extract_title(markdown)
        self.assertEqual("h1", extraction)
