import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_code,
    block_type_quote,
    block_type_heading,
    block_type_paragraph,
    block_type_olist,
    block_type_ulist,
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

# Tests for block_to_block_type

    def test_heading_block(self):
        block = "## this is a heading"
        assignment = block_to_block_type(block)
        self.assertEqual(block_type_heading, assignment)

    def test_invalid_heading_block(self):
        block = "##3 this is a heading"
        assignment = block_to_block_type(block)
        self.assertNotEqual(block_type_heading, assignment)

    def test_code_block(self):
        block = "``` this is code ```"
        assignment = block_to_block_type(block)
        self.assertEqual(block_type_code, assignment)

    def test_invalid_code_block(self):
        block = "`` this is code ```"
        assignment = block_to_block_type(block)
        self.assertNotEqual(block_type_code, assignment)

    def test_quote_block(self):
        block = "> this is a quote"
        assignment = block_to_block_type(block)
        self.assertEqual(block_type_quote, assignment)

    def test_invalid_quote_block(self):
        block = "''' this is quote '''"
        assignment = block_to_block_type(block)
        self.assertNotEqual(block_type_quote, assignment)

    def test_unordered_list_block(self):
        block = "* this is a unordered list"
        assignment = block_to_block_type(block)
        self.assertEqual(block_type_ulist, assignment)

    def test_invalid_unordered_list_block(self):
        block = "*this is invalid"
        assignment = block_to_block_type(block)
        self.assertNotEqual(block_type_ulist, assignment)

    def test_ordered_list_block(self):
        block = "1. this is a unordered list"
        assignment = block_to_block_type(block)
        self.assertEqual(block_type_olist, assignment)

    def test_invalid_ordered_list_block(self):
        block = "1.this is invalid"
        assignment = block_to_block_type(block)
        self.assertNotEqual(block_type_olist, assignment)

if __name__ == '__main':
    unittest.main()
