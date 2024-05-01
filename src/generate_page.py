import os
import shutil

from extract_title import extract_title
from markdown_blocks import markdown_to_html_nodes


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} ➡ {dest_path}")
    # Read the markdown file at from_path and store contents in a variable
    with open(from_path) as md_file:
        read_md_file = md_file.read()
    # print(f"The read markdown file is:\n{repr(read_md_file)}\n")
     # read the template file at template_path and store contents in a variable
    with open(template_path) as template_file:
        read_template = template_file.readlines()

    # utilize markdown_to_html_node function and .to_html() method to convert md file to HTML.
    html_converted_file = markdown_to_html_nodes(read_md_file)
    # print(f"{"*" * 70}\n{html_converted_file}\n {"*" * 70}")
    # extract title using extract_title function to get the title of the page
    document_title = extract_title(from_path)
    # print(f"The document title is: {document_title}")
    # replace {{Title}} and {{Content}} plaseholders in the template with the html and title you generated.
    # print(f"{"<>" * 70}\n{read_template}\n{len(read_template)}{"<>" * 70}")
    for line in read_template:
        if "{{ Title }}" in line:
            # print(f"The current value is {line}\n")
            line_index = read_template.index(line)
            read_template[line_index] = line.replace("{{ Title }}", document_title)
            # print(f"The updated line is: {line}")
        if "{{ Content }}" in line:
            # print(f"The current value is {line}\n")
            line_index = read_template.index(line)
            read_template[line_index] = line.replace("{{ Content }}", html_converted_file)
            # print(f"The updated line is: {line}")
    updated_html_document = "".join(read_template)
    # print(updated_html_document)

    # write the new HTML to a file at dest_path. Create all necesary directories if they don't exist
    #
    if os.path.exists(dest_path):
        final_path = os.path.join(dest_path, "index.html")
        with open(final_path, "w") as newfile:
            newfile.write(updated_html_document)
