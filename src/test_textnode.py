import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

from htmlnode import(
    LeafNode
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_convert_to_html_text(self):
        node = TextNode("I am some funny text", "text", None)
        self.assertTrue(node.text_node_to_html_node().__eq__(LeafNode(None, "I am some funny text", None)))

    def test_convert_to_html_bold(self):
        node = TextNode("This is a text node", "bold", None)
        self.assertTrue(node.text_node_to_html_node().__eq__(LeafNode("b", "This is a text node", None)))

    def test_convert_to_html_italic(self):
        node = TextNode("This is a text node", "italic", None)
        self.assertTrue(node.text_node_to_html_node().__eq__(LeafNode("i", "This is a text node", None)))

    def test_convert_to_html_code(self):
        node = TextNode("code text", "code", None)
        self.assertTrue(node.text_node_to_html_node().__eq__(LeafNode("code", "code text", None)))

    def test_convert_to_html_link(self):
        node = TextNode("some text", "link", "www.boot.dev")
        self.assertTrue(node.text_node_to_html_node().__eq__(LeafNode("a", "some text", {"href": "www.boot.dev"})))
        
if __name__ == "__main__":
    unittest.main()
