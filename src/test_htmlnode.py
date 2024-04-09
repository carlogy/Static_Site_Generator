import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_paragraph_node(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(
            node.props_to_html(),
            None
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(p, This is a paragraph, None, None)"
        )
    def test_anchor_tag_node(self):
        node = HTMLNode(
            "a",
            "www.google.com",
            None ,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(a, www.google.com, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        )
    def test_children_node(self):
        node = HTMLNode("p", None, [HTMLNode("p", "This is a p node as a child")])
        self.assertEqual(
            repr(node),
            'HTMLNode(p, None, [HTMLNode(p, This is a p node as a child, None, None)], None)'
        )
        self.assertEqual(
            node.props_to_html(),
            None
        )


if __name__ == "__main__":
    unittest.main()
