import re

from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
    TextNode
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if (node.text_type != text_type_text
            and node.text_type != text_type_bold
            and node.text_type != text_type_italic
            and node.text_type != text_type_code
            and node.text_typwe != text_type_link
            and node.text_type != text_type_image):
                new_nodes.append(node)
        sections = []
        splitsections = node.text.split(delimiter)
        if len(splitsections) % 2 == 0:
            raise ValueError("Invalid Markdown syntax")
        if len(splitsections) % 2 != 0:
            for i in range(len(splitsections)):
                if i % 2 == 0 and splitsections[i] != "":
                    sections.append(TextNode(splitsections[i], text_type_text, None))
                if i % 2 != 0:
                    sections.append(TextNode(splitsections[i], text_type))

                # This section only supports one markdown within the originalTextNode object
                #   eg. (This is **bold** and this  is not)
                #
                # if i  == 0 and splitsections[i] != "":
                #     sections.append(TextNode(splitsections[i], text_type_text, None))
                # if i  == 1:
                #     sections.append(TextNode(splitsections[i], text_type))
                # # if i > 1 and splitsections[i] != "":
                # #     sections.append(TextNode(splitsections[i], "text", None))
        new_nodes.extend(sections)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        images = extract_markdown_images(current_text)

        if len(images) == 0 and current_text != "":
            new_nodes.append(node)


        for image in images:
            split_images = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if not split_images[0] and split_images[1]:
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                current_text = split_images[1]
                continue
            if not split_images[0].strip() and not split_images[1]:
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                continue
            if split_images[0] and "![" in split_images[1]:
                new_nodes.append(TextNode(split_images[0], text_type_text))
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                current_text = split_images[1]
                continue
            if split_images[0] and not split_images[1]:
                new_nodes.append(TextNode(split_images[0], text_type_text))
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                continue

    return new_nodes

def split_nodes_links(old_nodes):
    pass
