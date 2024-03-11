import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML_match(self):
        html_node = HTMLNode("a", "Google", None ,{"href": "https://google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), ' href="https://google.com" target="_blank"')

class TestLeafNose(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(leaf_node.to_html(),'<p>This is a paragraph of text.</p>')

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_oarent_with_leaf_node(self):
        parent_node = ParentNode(
            "ol",
            [
                LeafNode("li", "This is item #1"),
                LeafNode("li", "This is item #2"),
                LeafNode("li", "This is item #3"),
                LeafNode("li", "This is item #4"),
            ],
        )
        self.assertEqual(parent_node.to_html(),'<ol><li>This is item #1</li><li>This is item #2</li><li>This is item #3</li><li>This is item #4</li></ol>')

    def test_parent_with_parent(self):
        parent_node = ParentNode(
            "section",
            [
                ParentNode("div",
                    [
                        LeafNode("p", "Paragraph 1"),
                        LeafNode("p", "Paragraph 2"),
                        LeafNode("p", "Paragraph 3"),
                    ],
                )
            ],
        )
        self.assertEqual(parent_node.to_html(), '<section><div><p>Paragraph 1</p><p>Paragraph 2</p><p>Paragraph 3</p></div></section>')

    def test_parent_empty_leaf(self):
        parent_node = ParentNode(
            "h1",
            [
                LeafNode("p", "This is a sentence."),
                ParentNode("h2",
                    [
                        LeafNode("p", "This is another sentence.")
                    ],)
            ],
        )

        self.assertEqual(parent_node.to_html(), '<h1><p>This is a sentence.</p><h2><p>This is another sentence.</p></h2></h1>')


if __name__ == "__main__":
    unittest.main()
