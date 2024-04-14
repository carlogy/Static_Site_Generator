import unittest

from textnode import TextNode

from inline_markdown import  (
    split_nodes_delimiter,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image)

class TestInlineMarkdown(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]

        )
    def test_regular_text_no_delimiter(self):
        node = TextNode("This is a sentance.", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [TextNode("This is a sentance.", "text", None)],
            new_nodes
        )
    def test_delimiter_at_end(self):
        node = TextNode("Text then **bold at end**", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Text then ", "text", None),
                TextNode("bold at end", "bold", None)
            ],
            new_nodes
        )

    def test_delimiter_at_beginning(self):
        node = TextNode("**Bold at start** text", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Bold at start", text_type_bold, None),
                TextNode(" text", "text", None)
            ],
            new_nodes
        )
    def test_empty(self):
        node = TextNode("", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        self.assertListEqual(
            [],
            new_nodes
        )
    def test_half_delimiter(self):
        node = TextNode("**Bold at start text", text_type_text, None)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_type_bold)

    def test_multiple_delimiters(self):
        node = TextNode("This **is** bold and **so** is this.", text_type_text, None)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This ", text_type_text, None),
                TextNode("is", text_type_bold, None),
                TextNode(" bold and ", text_type_text, None),
                TextNode("so", text_type_bold, None),
                TextNode(" is this.", text_type_text, None)
            ],
            new_nodes
        )



if __name__ == "__main__":
    unittest.main()
