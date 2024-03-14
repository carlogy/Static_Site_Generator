from htmlnode import LeafNode

 # text_type_text = "text"
 # text_type_bold = "bold"
 # text_type_italic = "italic"
 # text_type_code = "code"
 # text_type_link = "link"
 # text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,  OtherNode):
        return self.text == OtherNode.text and self.text_type == OtherNode.text_type and self.url == OtherNode.url

    def __repr__(self) -> str:
        return f"{self}({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):

    type = text_node.text_type
    text = text_node.text
    url = text_node.url

    if type == "text":
     return LeafNode(None, text)
    if type == "bold":
      return LeafNode("b", text)
    if type == "italic":
      return LeafNode("i", text)
    if type == "code":
        return LeafNode("code", text)
    if type == "link":
        return LeafNode("a", text, {"href" : url})
    if type == "img":
        return LeafNode("img","" ,{"src" : url, "alt" : text})

    raise Exception("Invalid TextNode passed: please pass a text node with a valid text_type(text, bold, italic, code, link, img).")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass
