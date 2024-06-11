class TextNode():
    def __init__(self, text, text_type, url):
        #the text content of the node
        self.text = text
        #type of text node contains (ie bold, italics, etc.)
        self.text_type = text_type
        #url of link or image if text is a link. Default to None if nothing passed in
        self.url = url

    def __eq__():
        if (text == self.text) and (text_type == self.text_type) and (url == self.url):
            return True

    def __repr__(self):
        return f"TextNode {self.text}, {self.text_type}, {self.url}"
