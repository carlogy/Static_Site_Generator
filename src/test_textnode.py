import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node1 = TextNode("This is text node node", "bold")
        self.assertNotEqual(node, node1)




if __name__ == "__main__":
    unittest.main()
