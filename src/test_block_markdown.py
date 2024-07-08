import unittest

from block_markdown import(
    markdown_to_blocks,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        text = "This is **bolded** paragraph\n\n\n This is another paragraph with *italic* text and `code` here\n This is the same paragraph on a new line\n\n *this is a list\n *with items"
        blocks = markdown_to_blocks(text)
        self.assertEqual(["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\n This is the same paragraph on a new line", "*this is a list\n *with items"],blocks)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

if __name__ == '__main':
    unittest.main()