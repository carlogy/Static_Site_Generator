import unittest
from markdown_blocks import block_to_block_type, markdown_to_blocks

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
    def test_block_to_block_type(self):

        markdown_blocks =  [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        block_to_block_type(markdown_blocks[0])



if __name__ == "__main__":
    unittest.main()
