import unittest

from htmlnode import (
    HTMLNode,
    prop_dict_test,
    type_test
)

class TestHTMLNode(unittest.TestCase):
    def test_props_eq(self):
        node = HTMLNode(None, None, None, {"A": "B", "C": "D"})
        self.assertEqual(
            ' A="B" C="D"', node.props_to_html()
        )

    def test_props_not_eq(self):
        node = HTMLNode(None, None, None, {"A": "B"})
        self.assertNotEqual(
            ' A="C"', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode("tag", "value", ["child", "child2"], prop_dict_test)
        self.assertEqual(
            "HTMLNode(tag, value, ['child', 'child2'], {'A': 'B', 'C': 'D'})", repr(node)
        )

    def test_repr_2(self):
        node = HTMLNode(type_test, "value", ["child", "child2"], {'A': 'B'})
        self.assertEqual(
            "HTMLNode(<a>, value, ['child', 'child2'], {'A': 'B'})", repr(node)
        )



if __name__ == "__main__":
    unittest.main()
