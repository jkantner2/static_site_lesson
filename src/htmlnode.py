prop_dict_test = {"A": "B", "C": "D"}
type_test = "<a>"

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        #String representing the HTML tag name (eg. "p", "a", "h1", etc.)
        self.tag = tag
        #String representing the value of the HTML tag (eg. the text inside a paragraph)
        self.value = value
        #List of HTMLNode objects representing the children of this NotADirectoryError
        self.children = children
        #Dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": :https://www.google.com"}
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implementd")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
