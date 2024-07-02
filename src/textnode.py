from htmlnode import (
    LeafNode
)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        #the text content of the node
        self.text = text
        #type of text node contains (ie bold, italics, etc.)
        self.text_type = text_type
        #url of link or image if text is a link. Default to None if nothing passed in
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(text_node):
        acceptable_type = ["text", "bold", "italic", "code", "link", "image"]
        if text_node.text_type not in acceptable_type:
            raise Exception("Invalid text node type")

        if text_node.text_type == "text":
            return LeafNode(None, text_node.text, None)

        if text_node.text_type == "bold":
            return LeafNode("b", text_node.text, None)

        if text_node.text_type == "italic":
            return LeafNode("i", text_node.text, None)

        if text_node.text_type == "code":
            return LeafNode("code", text_node.text, None)

        if text_node.text_type == "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})

        if text_node.text_type == "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    """@staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes: 
            if node.text_type != text_type_text:
                new_nodes.append(node)
                continue

            split_node = node.text.split(delimiter)

            if len(split_node) % 2 == 0:
                raise Exception("Invalid markdown syntax")

            x = node.text.split(delimiter)
            i = 0
            if delimiter == "`":
                while i <= len(x) - 1:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(x[i], text_type_text, None))
                        i += 1
                    else:
                        new_nodes.append(TextNode(x[i], text_type_code, None))
                        i += 1

            if delimiter == "**":
                while i <= len(x) - 1:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(x[i], text_type_text, None))
                        i += 1
                    else:
                        new_nodes.append(TextNode(x[i], text_type_bold, None))
                        i += 1

            if delimiter == "*":
                while i <= len(x) - 1:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(x[i], text_type_text, None))
                        i += 1
                    else:
                        new_nodes.append(TextNode(x[i], text_type_italic, None))
                        i += 1
        print(f"DD {new_nodes}")
        return new_nodes

#  
test_nodes = [
        TextNode("Big chungus `code hehe` nerd", text_type_text),
        TextNode("Some *italic* text", text_type_italic),
        TextNode("Some **bold** text", text_type_bold)
        ]

missing_closing_delimiter = TextNode("This is **a test", text_type_text)"""
