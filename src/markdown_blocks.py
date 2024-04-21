
from htmlnode import HTMLNode, LeafNode, ParentNode
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
        first_char = line[:1]

        match first_char:

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


def paragraph_block_to_htmlNode(block, block_type):

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
    list_items = [item.lstrip("*- ") for item in block.split("\n")]

    children_nodes = []
    for item in list_items:
        children_nodes.append(LeafNode("li", item, None))

    htmlNode = ParentNode("ul", children_nodes, None)

    return htmlNode


def ordered_list_block_to_htmlNode(block, block_type):
    list_items = [item.lstrip(f"{item[0]}. ") for item in block.split("\n")]

    children_nodes = []
    for item in list_items:
        children_nodes.append(LeafNode("li", item, None))

    htmlNode = ParentNode("ol", children_nodes, None)

    return htmlNode

def code_block_to_htmlNode(block, block_type):

    stripped_block = block.strip("` ")

    htmlNode = LeafNode("blockquote", stripped_block, None)

    return htmlNode


def markdown_to_html_nodes(markdown):

    markdown_blocks = markdown_to_blocks(markdown)

    for block in markdown_blocks:
        print(f"block:\n{block}\n")

        block_type = block_to_block_type(block)

        print(f"type:\n{block_type}\n")

    print(markdown_blocks)


#TO DO's with this function:
# takes a full markdown document and splits it into blocks
#
# use the split to blocks function
#
# top level should be div whith all the blocks being children
#
#
# blocks should have own inline children
