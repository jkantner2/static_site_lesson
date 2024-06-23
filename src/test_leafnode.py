import unittest

from htmlnode import (
    #HTMLNode,
    LeafNode,
    prop_dict_test,
    type_test,
    value_test
)

class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode("a", None, None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_value_no_tag(self):
        node = LeafNode(None, "this is a test", None, None) 
        self.assertEqual(node.to_html(), "this is a test")

    def test_child(self):
        node = LeafNode("a", "this is a test", ["entry", "entry2"], {"a":"b"})
        self.assertEqual('<a a="b">this is a test</a>', node.to_html())

if __name__ == "__main__":
    unittest.main()
