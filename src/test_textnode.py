import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is another text node", "bold", "https://notarealurl.com")
        node2 = TextNode("another text node", "italic", "https://yetanotherurl.com")
        self.assertNotEqual(node, node2)

    def test_None_url(self):
        node = TextNode("This is another node", "bold", None)
        node2 = TextNode("This is another node", "bold", "https//:google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
