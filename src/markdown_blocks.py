
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")

    scrubbed_blocks = [block.strip() for block in split_markdown if block != " "]

    return scrubbed_blocks

def block_to_block_type(block):

    lines_in_block = block.split("\n")

    for line in lines_in_block:
        # print(f"the current line: {line}")
        # print(f"the first characters in line: {line[:2]}\n {len(line[:2])}")
        first_two_chars = line[0]

        match first_two_chars:

            case "#":
                if line.startswith("# "):
                    return block_type_heading
                if line.startswith("## "):
                    return block_type_heading
                if line.startswith("### "):
                    return block_type_heading
                if line.startswith("#### "):
                    return block_type_heading
                if line.startswith("##### "):
                    return block_type_heading
                if line.startswith("###### "):
                    return block_type_heading
            case "`":
                if len(lines_in_block) > 1:
                    first_line_chars = lines_in_block[0][:3]
                    last_line_chars = lines_in_block[-1][:3]
                    if first_line_chars != "```" and last_line_chars != "```":
                        return block_type_paragraph
                if line[:3] != "```" and line[:-3] != "```":
                    return block_type_paragraph

                return block_type_code
            case ">":
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        if first_chars != "> ":
                            return block_type_paragraph
                        i += 1
                return block_type_quote
            case "*":
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        print(first_chars)
                        if first_chars != "* " and first_chars != "- ":
                            return block_type_paragraph
                        i += 1
                    return block_type_unordered_list
            case "1" :
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        if first_chars != f"{i + 1}.":
                            return block_type_paragraph
                        i += 1
                return block_type_ordered_list
            case _:
                return block_type_paragraph


def paragraph_block_to_html(block, block_type):

    if block_type != block_type_paragraph:
        raise ValueError("invalid blocktype.")
    paragraph_node = LeafNode("p", block, None)
    return paragraph_node


def heading_block_to_htmlNode(block, block_type):

    if block_type != block_type_heading:
        raise ValueError("invalid blocktype.")
    count = 0
    for char in block:
        if char == "#":
            count += 1
    heading_node = LeafNode(f"h{count}", block.lstrip("# "), None)
    return heading_node

def unorderd_list_block_to_htmlNode(block, block_type):
    pass

def ordered_list_block_to_htmlNode(block, block_type):
    pass

def quote_block_to_htmlNode(block, block_type):
    pass
