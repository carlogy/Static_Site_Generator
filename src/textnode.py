class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, otherNode):
        return(
            self.text_type == otherNode.text_type
            and self.text == otherNode.text
            and self.url == otherNode.url
        )
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
