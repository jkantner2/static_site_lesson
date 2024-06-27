prop_dict_test = {"A": "B", "C": "D"}
type_test = "<a>"
value_test = "this is a test"

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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self): 
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return NotImplemented

        return (
            self.tag == other.tag 
            and self.value == other.value
            and self.props == other.props
        )

class ParentNode(HTMLNode): 
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided when tag is required")
        if self.children == None:
            raise ValueError("No child nodes listed when parent nodes require children")
        temp = ""
        for node in self.children:
            if node.children is None:
                temp += node.to_html()
            else:
                temp += node.to_html()
        return f"<{self.tag}>{temp}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
