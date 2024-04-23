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
            and node.text_type != text_type_link
            and node.text_type != text_type_image):
                new_nodes.append(node)
        sections = []
        splitsections = node.text.split(delimiter)

        if len(splitsections) % 2 == 0:
            raise ValueError("Invalid Markdown syntax")
        if len(splitsections) % 2 != 0:
            for i in range(len(splitsections)):
                if i % 2 == 0 and splitsections[i] != "" and splitsections[i] != " ":
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
        # print(f"images that were extracted :{images}\n")
        # if len(images) == 0:
        #     new_nodes.append(node)
        for image in images:
            # print(f"the current image we are iterating over is: {image}\n")
            # print(f"The current text is: {current_text}\n")
            image_alt_text = image[0]
            image_src = image[1]
            split_image_text = current_text.split(f"![{image[0]}]({image[1]})", 1)
            # print(f"the current text split by image string literal is: {split_image_text}\n")
            if len(split_image_text[0]) != 0 and split_image_text[1]:
                new_nodes.append(TextNode(split_image_text[0], text_type_text))
                new_nodes.append(TextNode(image_alt_text, text_type_image, image_src))
                current_text = split_image_text[1]
                continue
            if len(split_image_text[0]) == 0 and split_image_text[1]:
                new_nodes.append(TextNode(image_alt_text, text_type_image, image_src))
                current_text = split_image_text[1]
                continue
            if len(split_image_text[0].strip()) == 0 and len(split_image_text[1]) == 0:
                new_nodes.append(TextNode(image_alt_text, text_type_image, image_src))
                current_text = split_image_text[1]
                continue
            if len(split_image_text[0]) != 0 and not len(split_image_text[1]):
                new_nodes.append(TextNode(split_image_text[0], text_type_text))
                new_nodes.append(TextNode(image_alt_text, text_type_image, image_src))
                current_text = split_image_text[1]
                continue
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))

    return new_nodes


# ORIGINAL IMPLEMENTATION
# def split_nodes_images(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         current_text = node.text
#         images = extract_markdown_images(current_text)

#         if len(images) == 0 and current_text != "":
#             new_nodes.append(node)


#         for image in images:
#             split_images = current_text.split(f"![{image[0]}]({image[1]})", 1)
#             if not split_images[0] and split_images[1]:
#                 new_nodes.append(TextNode(image[0], text_type_image, image[1]))
#                 current_text = split_images[1]
#                 continue
#             if not split_images[0].strip() and not split_images[1]:
#                 new_nodes.append(TextNode(image[0], text_type_image, image[1]))
#                 continue
#             if split_images[0] and "![" in split_images[1]:
#                 new_nodes.append(TextNode(split_images[0], text_type_text))
#                 new_nodes.append(TextNode(image[0], text_type_image, image[1]))
#                 current_text = split_images[1]
#                 continue
#             if split_images[0] and not split_images[1]:
#                 new_nodes.append(TextNode(split_images[0], text_type_text))
#                 new_nodes.append(TextNode(image[0], text_type_image, image[1]))
#                 continue

#     return new_nodes
#
def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text
        links = extract_markdown_links(current_text)


        for link in links:

            link_anchor_text = link[0]
            url = link[1]
            split_link_text = current_text.split(f"[{link[0]}]({link[1]})", 1)

            if len(split_link_text[0]) != 0 and split_link_text[1]:
                new_nodes.append(TextNode(split_link_text[0], text_type_text))
                new_nodes.append(TextNode(link_anchor_text, text_type_link, url))
                current_text = split_link_text[1]
                continue
            if len(split_link_text[0]) == 0 and split_link_text[1]:
                new_nodes.append(TextNode(link_anchor_text, text_type_link, url))
                current_text = split_link_text[1]
                continue
            if len(split_link_text[0].strip()) == 0 and len(split_link_text[1]) == 0:
                new_nodes.append(TextNode(link_anchor_text, text_type_link, url))
                current_text = split_link_text[1]
                continue
            if len(split_link_text[0]) != 0 and not len(split_link_text[1]):
                new_nodes.append(TextNode(split_link_text[0], text_type_text))
                new_nodes.append(TextNode(link_anchor_text, text_type_link ,url))
                current_text = split_link_text[1]
                continue
        if current_text != "":
            new_nodes.append(TextNode(current_text, text_type_text))

    return new_nodes

# This is the original implementation of split_nodes_links:

# def split_nodes_links(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         current_text = node.text
#         links = extract_markdown_links(current_text)

#         if len(links) == 0 and current_text != "":
#             new_nodes.append(node)

#         for link in links:
#             split_links = current_text.split(f"[{link[0]}]({link[1]})", 1)

#             if not split_links[0] and split_links[1]:
#                 new_nodes.append(TextNode(link[0], text_type_link, link[1]))
#                 current_text = split_links[1]
#                 continue
#             if not split_links[0].strip() and not split_links[1]:
#                 new_nodes.append(TextNode(link[0], text_type_link, link[1]))
#                 continue
#             if split_links[0] and "[" in split_links[1]:
#                 new_nodes.append(TextNode(split_links[0], text_type_text))
#                 new_nodes.append(TextNode(link[0], text_type_link, link[1]))
#                 current_text = split_links[1]

#             if split_links[0] and not split_links[1]:
#                 new_nodes.append(TextNode(split_links[0], text_type_text))
#                 new_nodes.append(TextNode(link[0], text_type_link, link[1]))
#                 continue

#     return new_nodes

def text_to_textnodes(text):


    starting_node = [TextNode(text, text_type_text)]



    new_nodes = []

    split_node_list = split_nodes_delimiter(starting_node, "**", text_type_bold)
    new_nodes.extend(split_node_list[:-1])

    split_node_list = split_nodes_delimiter([split_node_list[-1]], "*", text_type_italic)
    new_nodes.extend(split_node_list[:-1])

    split_node_list = split_nodes_delimiter([split_node_list[-1]], "`", text_type_code)
    new_nodes.extend(split_node_list[:-1])

    split_node_list = split_nodes_images([split_node_list[-1]])
    new_nodes.extend(split_node_list[:-1])


    split_node_list = split_nodes_links([split_node_list[-1]])
    new_nodes.extend(split_node_list)

    return new_nodes
