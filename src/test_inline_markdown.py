import unittest

from textnode import TextNode



from inline_markdown import  (
    extract_markdown_images,
    extract_markdown_links,
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

    def test_image_extraction(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            (
                "another",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png"
            )
        ]
        self.assertListEqual(
            extract_markdown_images(text),
            images
        )

    def test_empty_image_string(self):
        text = ""
        self.assertListEqual(
            extract_markdown_images(text),
            []
        )

    def test_no_images_strint(self):
        text = "There are no images in this string"
        self.assertListEqual(
            extract_markdown_images(text),
            []
        )

    def test_img_beginning(self):
        text = "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) that's an image"
        images = [
            (
                "image",
                "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"
            )
        ]
        self.assertListEqual(
            extract_markdown_images(text),
            images
        )




    def test_link_extraction(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = [
            (
                "link",
                "https://www.example.com"
            ),
            (
                "another",
                "https://www.example.com/another"
            )
        ]
        self.assertListEqual(
            extract_markdown_links(text),
            links
        )

    def test_empty_link_string(self):
        text = ""
        self.assertListEqual(
            extract_markdown_links(text),
            []
        )

    def test_no_links_string(self):
        text = "There are no images in this string"
        self.assertListEqual(
            extract_markdown_links(text),
            []
        )

    def test_links_beginning_string(self):
        text = "[link](https://www.google.com) that's a link"
        links = [
            (
                "link",
                "https://www.google.com"
            )
        ]
        self.assertListEqual(
            extract_markdown_links(text),
            links
        )




if __name__ == "__main__":
    unittest.main()
