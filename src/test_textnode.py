import unittest

from htmlnode import LeafNode
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", "bold")
        node2 = TextNode("This is a bold text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is an italic text node", "italic")
        node1 = TextNode("This is a bold text node node", "bold")
        self.assertNotEqual(node, node1)

    def test_text_node_to_html_node(self):
       node = TextNode("This is a bold text node", "bold")
       self.assertEqual(
           node.text_node_to_html_node(),
           LeafNode("b", "This is a bold text node", None)
       )
    def test_text_node_link_to_html(self):
        node = TextNode("Click Me!", "link","https://www.google.com")
        leaf = LeafNode("a", "Click Me!", {"href" : "https://www.google.com" })
        self.assertEqual(
            node.text_node_to_html_node(),
            leaf
        )

    def test_code_node_to_html(self):
        node = TextNode("Hello World!", "code", None)
        leaf = LeafNode("code", "Hello World!", None)
        self.assertEqual(
            node.text_node_to_html_node(),
            leaf
        )

    def test_image_node_to_html(self):
        node = TextNode(
                            "bootDev",
                            "image",
                            "https://www.boot.dev/_nuxt/bootdev-logo-full-small.T5Eqr5qH.png"
        )
        leaf = LeafNode(
                            "img",
                            "",
                            {"src" : "https://www.boot.dev/_nuxt/bootdev-logo-full-small.T5Eqr5qH.png",
                            "alt" : "bootDev"
                            }
        )
        self.assertEqual(
            node.text_node_to_html_node(),
            leaf
        )

if __name__ == "__main__":
    unittest.main()
