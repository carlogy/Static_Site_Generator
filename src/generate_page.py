import os
import shutil

from extract_title import extract_title
from markdown_blocks import markdown_to_html_nodes


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} ➡ {dest_path}")

    with open(from_path) as md_file:
        read_md_file = md_file.read()

    with open(template_path) as template_file:
        read_template = template_file.readlines()


    html_converted_file = markdown_to_html_nodes(read_md_file)
    document_title = extract_title(from_path)
    for line in read_template:
        if "{{ Title }}" in line:
            line_index = read_template.index(line)
            read_template[line_index] = line.replace("{{ Title }}", document_title)
        if "{{ Content }}" in line:
            line_index = read_template.index(line)
            read_template[line_index] = line.replace("{{ Content }}", html_converted_file)
    updated_html_document = "".join(read_template)

    if os.path.exists(dest_path):
        final_path = os.path.join(dest_path, "index.html")
        with open(final_path, "w") as newfile:
            newfile.write(updated_html_document)
