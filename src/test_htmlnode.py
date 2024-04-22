import unittest

from htmlnode  import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_paragraph_node(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(
            node.props_to_html(),
            ""
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
            ""
        )
    def test_no_tag_leaf(self):
        leafnode = LeafNode(None,"This is just raw text",None)
        self.assertEqual(
            leafnode.to_html(),
            "This is just raw text"
        )
    def test_paragraph_leaf(self):
        leafnode = LeafNode("p", "This is a paragraph", None)
        self.assertEqual(
            leafnode.to_html(),
            "<p>This is a paragraph</p>"
        )
    def test_anchor_link_leaf(self):
        leafnode = LeafNode("a", "Click me!", {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(
            leafnode.to_html(),
            '<a href="https://www.google.com" target="_blank">Click me!</a>'
        )
    def test_no_value_leaf(self):
        leafnode = LeafNode("p",None,None)
        with self.assertRaises(ValueError):
            leafnode.to_html()

    def test_repr_Leaf(self):
        leafnode = LeafNode("p", "This is a paragraph", None)
        self.assertEqual(
            repr(leafnode),
            "LeafNode(p, This is a paragraph, None)"
        )
    def test_parent_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {'href': 'https://www.google.com', 'target': '_blank'}),
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text",None),
            ],
            None
        )
        self.assertEqual(
            node.to_html(),
            '<p><b href="https://www.google.com" target="_blank">Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_parent_no_tag(self):
        node = ParentNode(
            None,
            [LeafNode(None, "Normal text", None),],
            None
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("b", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr_Parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode(None, "Normal text", None),
                LeafNode("i", "italic text", None),
                LeafNode(None, "Normal text", None),
            ],
            None
        )
        self.assertEqual(
            repr(node),
            "ParentNode(p, [LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)"
        )


if __name__ == "__main__":
    unittest.main()
