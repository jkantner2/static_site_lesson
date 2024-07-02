import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    #test_nodes,
    #missing_closing_delimiter
)

from htmlnode import(
    LeafNode
)

class TestTextNode(unittest.TestCase):

# Unit tests for __eq__ and __repr__ override functions

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

# Unit tests for covernt to hmtl function

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
        
# Unit tests for split by delimiter filter

    """def test_single_split_and_nontext_text_type(self):
        node = test_nodes
        new_nodes = TextNode.split_nodes_delimiter(node, "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("Big chungus ", text_type_text),
            TextNode("code hehe", text_type_code),
            TextNode(" nerd", text_type_text),
            TextNode("Some *italic* text", text_type_italic),
            TextNode("Some **bold** text", text_type_bold)
            ])

    def test_no_closing_delimiter(self):
        node = missing_closing_delimiter
        with self.assertRaises(Exception):
            TextNode.split_nodes_delimiter(node, "**", text_type_bold)

    def test_invalid_text_type_TextNode(self):
        node = TextNode("this is *a* test", "invalid")
        with self.assertRaises(Exception):
            TextNode.split_nodes_delimiter(node, "*", text_type_italic)

    def test_delim_bold_double(self):
        node = TextNode(
                "This is text with **two** bold **words**", text_type_text
            )
        new_nodes = TextNode.split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(
            [
                TextNode("This is text with ", text_type_text),
                TextNode("two", text_type_bold),
                TextNode(" bold ", text_type_text),
                TextNode("words", text_type_bold),
            ],
            new_nodes,
        )"""



if __name__ == "__main__":
    unittest.main()
