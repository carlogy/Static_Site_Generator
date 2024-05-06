import os
import shutil

from markdown_blocks import markdown_to_blocks, markdown_to_html_nodes
from extract_title import extract_title

def generate_pages(dir_path_content, template_path, dest_dir_path):
    # should crawl every entry in the dir_path_content directory and generate .html page # for each markdown file it finds
    print(f"Generating pages from  {dir_path_content}")
    dir_path_files = list(os.scandir(dir_path_content))
    for entry in dir_path_files:
        if entry.is_file():
            dest_file_path = f"{dest_dir_path}{entry.path.removeprefix("./content").removesuffix(".md")}.html"
            print(f"The file path: {entry.path}\n")
            with open(entry.path) as md_file:
                read_md_file = md_file.read()

            with open(template_path) as template_file:
                read_template = template_file.readlines()

            html_converted_file = markdown_to_html_nodes(read_md_file)
            document_title = extract_title(entry.path)
            for line in read_template:
                if "{{ Title }}" in line:
                    line_index = read_template.index(line)
                    read_template[line_index] = line.replace("{{ Title }}", document_title)
                if "{{ Content }}" in line:
                    line_index = read_template.index(line)
                    read_template[line_index]  = line.replace("{{ Content }}", html_converted_file)
            updated_html_document = "".join(read_template)

            with open(dest_file_path, "w") as new_file:
                new_file.write(updated_html_document)

        if entry.is_dir():
            dest_file_path = f"{dest_dir_path}{entry.path.removeprefix("./content")}"
            if not os.path.exists(dest_file_path):
                os.mkdir(dest_file_path)
            generate_pages(entry.path, template_path, dest_dir_path)
