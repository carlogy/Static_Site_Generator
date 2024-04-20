
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")

    # print(f"Original markdown input to process:\n {markdown}\n")

    # print(f"split markdown list by new line\n {split_markdown}\n")

    # Need to clean up the list to remove white spacing and empty text blocks

    scrubbed_blocks = [block.strip() for block in split_markdown if block != " "]
    # print(f"scrubbed blocks list:\n {scrubbed_blocks} ")

    return scrubbed_blocks

def block_to_block_type(block):

    # print(f"Block: {block}")

    lines_in_block = block.split("\n")

    # print(f"Split by new line list:\n{lines_in_block}")

    for line in lines_in_block:
        print(f"the current line: {line}")
        print(f"the first characters in line: {line[:2]}\n {len(line[:2])}")
        first_two_chars = line[0]

        match first_two_chars:

            case "#":
                return block_type_heading
            case "`":
                if len(lines_in_block) > 1:
                    first_line_chars = lines_in_block[0][:3]
                    last_line_chars = lines_in_block[-1][:3]
                    if first_line_chars != "```" and last_line_chars != "```":
                        raise ValueError("Invalid quote markdown")
                if line[:3] != "```" and line[:-3] != "```":
                    raise ValueError("Invalid quote markdown")

                return block_type_code
            case ">":
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        if first_chars != "> ":
                            raise ValueError("Invalid quote markdown")
                        i += 1
                return block_type_quote
            case "*":
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        print(first_chars)
                        if first_chars != "* " and first_chars != "- ":
                            raise ValueError(f"Invalid unordered list markdown\n{lines_in_block[i][:2]}, {len(lines_in_block[i][:2])}")
                        i += 1
                    return block_type_unordered_list

            case "1" :
                if len(lines_in_block) > 1:
                    i = 0
                    while i < len(lines_in_block):
                        first_chars = lines_in_block[i][:2]
                        if first_chars != f"{i + 1}.":
                            raise ValueError(f"Invalid ordered list markdown.\n{first_chars}, {len(first_chars)} {i}.")
                        i += 1
                return block_type_ordered_list
            case _:
                return block_type_paragraph
