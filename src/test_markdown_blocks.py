import unittest

from htmlnode import LeafNode
from markdown_blocks import (
    block_to_block_type,
    heading_block_to_html,
    markdown_to_blocks,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
    paragraph_block_to_html
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_multi_line_block(self):
        markdown_text = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"

        markdown_blocks = markdown_to_blocks(markdown_text)
        self.assertListEqual(
            markdown_blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )

    def test_empty_block(self):
        markdown_text = "#This is a header\n\n \n\n This is a paragraph on which a preceding white space exists"
        markdown_blocks = markdown_to_blocks(markdown_text)
        self.assertListEqual(
            markdown_blocks,
            [
                "#This is a header",
                "This is a paragraph on which a preceding white space exists"
            ]
        )

    def test_extra_newlines_trailing_white_space(self):
        markdown = "##This is a smaller header\n\n\n###This is a smaller header\n\nThis is a paragraph with a space at the end "
        markdown_blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            markdown_blocks,
            [
                "##This is a smaller header",
                "###This is a smaller header",
                "This is a paragraph with a space at the end"
            ]
        )
    def test_heading_block(self):

        markdown_block = "## This is a smaller header"
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(
            block_type,
            block_type_heading
        )

    def test_unorder_list_block(self):

        markdown_block ="This is a **paragraph**."
        block_type = block_to_block_type(markdown_block)
        self.assertEqual(
            block_type,
            block_type_paragraph
        )

    def test_ordered_list_block(self):
        markdown_text = "1. This the first item in ordered list\n2. This is the second item.\n3. This is the third item."
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_ordered_list
        )

    def test_single_ordered_list(self):
        markdown_test = "1. This a single list item."
        block_type = block_to_block_type(markdown_test)
        self.assertEqual(
            block_type,
            block_type_ordered_list
        )

    def test_code_block(self):
        markdown_text = "``` def hello_world():\n\tprint('Hello World!') ```"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_code
        )

    def test_quote_block(self):
        markdown_text = "> This is a quote\n> and another line of for a quote"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_quote
        )

    def test_not_mixed_unorded_list(self):
        markdown_text = "* This is an unordered list item\n- this is a second list item"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_unordered_list
        )

    def test_not_sequential_ordered_list(self):
        markdown_text = "1. This is an ordered list item\n3. This is another ordered list item out of order"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_paragraph
        )

    def test_not_valid_quote(self):
        markdown_text = "` This is an invalid quote markdown text string `"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(
            block_type,
            block_type_paragraph
        )

    def test_paragraph_to_HtmlNode(self):
        markdown = "This is a paragraph of text\nWith a another line of text in same text block."
        block_type = block_to_block_type(markdown)
        htmlNode = paragraph_block_to_html(markdown, block_type)
        self.assertEqual(
            htmlNode,
            LeafNode("p", "This is a paragraph of text\nWith a another line of text in same text block.", None)
        )

    def test_heading1_to_HtmlNode(self):
        markdown = "# This is a heading"
        block_type = block_to_block_type(markdown)
        htmlNode = heading_block_to_html(markdown, block_type)

        self.assertEqual(
            htmlNode,
            LeafNode("h1", "This is a heading", None)
        )




if __name__ == "__main__":
    unittest.main()
