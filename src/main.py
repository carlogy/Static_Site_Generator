import os
import shutil

from copy_directory import copy_directory
from extract_title import extract_title
from generate_page import generate_page

puclic_dir_path = "./public"
static_dir_path = "./static"


def main():
    print("Deleting public directory...")
    if os.path.exists(puclic_dir_path):
        shutil.rmtree(puclic_dir_path)
    print("Copying static files to public directory...")
    copy_directory(static_dir_path)
    generate_page("./content/index.md", "./template.html", "./public")

main()
