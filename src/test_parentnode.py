import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)

class TestParentNode(unittest.TestCase):
    def test_parent(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())
    
    def test_parent_nested(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        ParentNode(
            "p",
            [
                LeafNode("i", "italic text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text")
                    ]
                )
            ]
        ),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual("<p><b>Bold text</b><p><i>italic text</i><p><b>Bold text</b></p></p>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def no_children(self):
        node = ParentNode("p", "some value")
        with self.assertRaises(ValueError):
            node.to_html()


    def no_tag(self):
        node = ParentNode(None, [LeafNode(None, "Normal text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = ParentNode("p", [LeafNode(None, "Normal text")], {"A": "B"})
        self.assertEqual("ParentNode(p, [LeafNode(None, Normal text, None)], {'A': 'B'})",node.__repr__())

if __name__ == "__main__":
    unittest.main()
