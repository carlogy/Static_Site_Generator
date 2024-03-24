import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images
)

from textnode import TextNode

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_not_in_text(self):
        node = TextNode("None formatted text", "text")
        self.assertEqual(
            split_nodes_delimiter([node], "*", "text"),
            [TextNode("None formatted text", "text")]
        )

    def test_bold_delim(self):
        node = TextNode("This is **bold**.", "text")
        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("bold", "bold"),
                TextNode(".", "text")
            ],
            split_nodes_delimiter([node], "**", "bold")
        )

    def test_multiple_bold_within_text(self):
        node = TextNode("This is **bold** and so is **this**", "text")
        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("bold", "bold"),
                TextNode(" and so is ", "text"),
                TextNode("this", "bold")
            ],
            split_nodes_delimiter([node], "**", "bold")
        )

    def test_invalid_input(self):
        node = TextNode("This has **bad markdown", "text")
        self.assertRaises(
            Exception,
            msg="Invalid Markdown syntax: The provided node does not have the correct Markdown syntax."

        )

    def test_non_text_node(self):
        node = [
            TextNode("This is **bold**", "text"),
            "Non-TextNode object",
            TextNode("**This too**", "text")
        ]

        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("bold", "bold"),
                "Non-TextNode object",
                TextNode("This too", "bold")
            ],
            split_nodes_delimiter(node, "**", "bold")
        )

    def text_code_block_node(self):
        node = TextNode("This is sentance with a `code block` word", "text")

        self.assertListEqual(
            [
                TextNode("This is sentance with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            split_nodes_delimiter([node], "`", "code")
        )

    def test_italic_node(self):
        node = TextNode("This is a sentence with an *italic* word", "text")

        self.assertListEqual(
            [
                TextNode("This is a sentence with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            split_nodes_delimiter([node], "*", "italic"),
        )

    def test_multiple_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png")
            ],
            extract_markdown_images(text)
        )

    def test_multiple_links(self):
        text = text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ],
            extract_markdown_links(text)

        )

    def test_no_images(self):
        text = "This text doesn't include images."
        self.assertListEqual(
            [],
            extract_markdown_images(text)
        )

    def test_no_links(self):
        text = "This text doesn't include links."
        self.assertListEqual(
            [],
            extract_markdown_links(text)
        )






if __name__ == "__main__":
    unittest.main()
