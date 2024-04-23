
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):

    split_markdown = markdown.split("\n\n")

    scrubbed_blocks = [block.strip() for block in split_markdown if block != "" or block != " "]

    if "" in scrubbed_blocks:
        scrubbed_blocks.remove("")

    return scrubbed_blocks

def block_to_block_type(block):

    lines_in_block = block.split("\n")

    for line in lines_in_block:

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
                return block_type_paragraph
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
                        if not lines_in_block[i].startswith("* "):
                            return block_type_paragraph
                        i += 1
                return block_type_unordered_list
            case "-":
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        if not lines_in_block[i].startswith("- "):
                            return block_type_paragraph
                        i += 1
                return block_type_unordered_list
            case "1" :
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        if not lines_in_block[i].startswith(f"{i + 1}. "):
                            return block_type_paragraph
                        i += 1
                return block_type_ordered_list
            case _:
                return block_type_paragraph


def paragraph_block_to_htmlNode(block, block_type):

    if block_type != block_type_paragraph:
        raise ValueError("invalid block type.")

    inline_children = text_to_textnodes(block)

    html_children_Nodes = [child.text_node_to_html_node() for child in inline_children]

    paragraph_node = ParentNode("p", html_children_Nodes, None)

    return paragraph_node


def heading_block_to_htmlNode(block, block_type):

    if block_type != block_type_heading:
        raise ValueError("invalid block type.")

    inline_children = "".join([child.lstrip("# ") for child in block.split("\n")])

    inline_children = text_to_textnodes(inline_children)

    html_children_Nodes = [child.text_node_to_html_node() for child in inline_children]

    count = 0
    for char in block:
        if char == "#":
            count += 1
    heading_node = ParentNode(f"h{count}", html_children_Nodes, None)

    return heading_node

def unordered_list_block_to_htmlNode(block, block_type):

    if block_type != block_type_unordered_list:
        raise ValueError(f"invalid block type\n{block_type}\nThe block:\n{block}")

    list_items = [item.lstrip("*- ") for item in block.split("\n")]

    children_nodes = []
    for item in list_items:
        child = text_to_textnodes(item)
        child_html_node = child[0].text_node_to_html_node()
        if child_html_node.tag == None:
            child_html_node.tag = "li"
            children_nodes.append(child_html_node)
            continue
        if child_html_node.tag != None:
            parent_node_for_child = ParentNode("li", [child_html_node], None)
            children_nodes.append(parent_node_for_child)

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

    code_lines = block.strip("` ")

    code_text_nodes = text_to_textnodes(code_lines)

    html_children_nodes = [child.text_node_to_html_node() for child in code_text_nodes]

    code_html_children = ParentNode("code", html_children_nodes, None)

    htmlNode = ParentNode("pre", [code_html_children], None)

    return htmlNode

def quote_block_to_htmlNode(block, block_type):

    quote_lines = "".join([line.lstrip(" ") for line in block.split(">")])

    quote_text_nodes = text_to_textnodes(quote_lines)

    html_children_nodes = [child.text_node_to_html_node() for child in quote_text_nodes]

    htmlNode = ParentNode("blockquote", html_children_nodes, None)

    return htmlNode

def markdown_to_html_nodes(markdown):

    markdown_blocks = markdown_to_blocks(markdown)

    html_nodes = []

    for block in markdown_blocks:

        block_type = block_to_block_type(block)

        match block_type:

            case "paragraph":

                paragraph_node = paragraph_block_to_htmlNode(block, block_type)

                html_nodes.append(paragraph_node)
                continue
            case "heading":
                heading_node = heading_block_to_htmlNode(block, block_type)
                html_nodes.append(heading_node)
                continue
            case "code":
                code_node = code_block_to_htmlNode(block, block_type)
                html_nodes.append(code_node)
                continue
            case "unordered_list":
                unordered_list_node = unordered_list_block_to_htmlNode(block, block_type)
                html_nodes.append(unordered_list_node)
                continue
            case "ordered_list":
                ordered_list_node = ordered_list_block_to_htmlNode(block, block_type)
                html_nodes.append(ordered_list_node)
                continue
            case "quote":
                quote_list_node = quote_block_to_htmlNode(block, block_type_quote)
                html_nodes.append(quote_list_node)
                continue

    main_component = ParentNode("div", html_nodes, None)

    html_document = main_component.to_html()

    return html_document
