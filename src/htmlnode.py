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
        raise NotImplementedError

    def props_to_html(self):
        for key, value in self.props:
            return " " + key + "=" + '"' + value + '"'

    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props},"
