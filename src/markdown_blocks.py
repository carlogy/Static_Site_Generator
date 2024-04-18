def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")


    # print(f"Original markdown input to process:\n {markdown}\n")

    # print(f"split markdown list by new line\n {split_markdown}\n")

    # Need to clean up the list to remove white spacing and empty text blocks
    #
    scrubbed_blocks = [block.strip() for block in split_markdown if block != " "]
    # print(f"scrubbed blocks list:\n {scrubbed_blocks} ")

    return scrubbed_blocks
