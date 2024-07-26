import unittest
from markdown_to_htmlnode import *

class TestMarkdownToHtmlnode(unittest.TestCase):
    def test_markdown_to_htmlnode(self):
        text = """
This is a paragraph
"""
#```This is code```

#> This is a quote

#* Unordered list entry 1
#* Unordered list entry 2

#1. Ordered list entry 1
#2. Ordered list entry 2

### This is a heading

        nodes = markdown_to_htmlnode(text)
        self.assertEqual(
            ParentNode("div",
                [
                    ParentNode("p", [
                        LeafNode(None, "This is a paragraph"),
#                    LeafNode("b", "bold"),
#                    LeafNode(None, " text")
                    ]),
#                HTMLNode("pre", None, [
#                    LeafNode("code", "This is code")
#                    ]),
#                HTMLNode("blockquote", None, [
#                    LeafNode(None, "This is a quote")
#                    ]),
#                HTMLNode("ul", None, [
#                    HTMLNode("li", "Unordered list entry 1"),
#                    HTMLNode("li", "Unordered list entry 2")
#                    ]),
#                HTMLNode("ol", None, [
#                    HTMLNode("li", "Ordered list entry 1"),
#                    HTMLNode("li", "Ordered list entry 2")
#                    ]),
#                HTMLNode("h3", None, [
#                    LeafNode(None, "This is a heading")
#                    ])
                ], 
                None
                ),
                nodes
                )



if __name__ == "__main__":
    unittest.main()
