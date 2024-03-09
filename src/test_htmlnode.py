import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def props_to_HTML_match(self):
        html_node = HTMLNode("a", "Google", None ,{"href": "https://google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), ' href="https://google.com" target="_blank"')

class TestLeafNose(unittest.TestCase):
    def to_html(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(leaf_node.to_html(),'<p>This is a paragraph of text.</p>')


if __name__ == "__main__":
    unittest.main()
