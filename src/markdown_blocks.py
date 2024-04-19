
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type__ordered_list = "ordered_list"




def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")


    # print(f"Original markdown input to process:\n {markdown}\n")

    # print(f"split markdown list by new line\n {split_markdown}\n")

    # Need to clean up the list to remove white spacing and empty text blocks
    #
    scrubbed_blocks = [block.strip() for block in split_markdown if block != " "]
    # print(f"scrubbed blocks list:\n {scrubbed_blocks} ")

    return scrubbed_blocks


def block_to_block_type(block):

    print(f"Block: {block}")

    lines_in_block = block.split("\n")

    print(f"Split by new line list:\n{lines_in_block}")

    for line in lines_in_block:
        match line[0]:
            case "#":
                return block_type_heading
            case "```":
                return block_type_code
            case ">":
                if len(lines_in_block) > 1:
