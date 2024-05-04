
from markdown_blocks import markdown_to_blocks


def extract_title(markdown):
     # open a markdown file
     with open(markdown) as file:
         read_file = file.read()
     # look for # header element in file

     # print(repr(read_file))

     md_blocks = markdown_to_blocks(read_file)
     # print(md_blocks)

     # extract the text and return it
     for line in md_blocks:
         if line.startswith("# "):
             return line.removeprefix("# ")
     # exception handle a file not having an # element in the file msg: "All pages need a single h1 header"
     raise ValueError("All pages need a single h1 header.")
