from genericpath import isdir
import os

from textnode import TextNode


def main():
    node = TextNode("This is a node", "bold", "https://www.boot.dev")
    print(repr(node))

    def search_dir_contents(path):
        static_dir = path
        if not os.path.exists(static_dir):
            raise IsADirectoryError("The directory does not exist, or system permissions for this directory are not granted.\n Run ls -l (dir_path) to view permission.\nTo modify with chomd.")

        if os.path.exists(static_dir):
            current_file_structure = os.listdir(static_dir)
            with os.scandir(static_dir) as scan_current_dir:
                for entry in scan_current_dir:
                    if entry.is_file():
                        print(f"Is file: {entry}")
                    if entry.is_dir():
                        print(f"is Directory:{entry}")
                        sub_path = os.path.join(entry)
                        if os.path.exists(sub_path):
                            print("It exists!")
                            with os.scandir(sub_path) as scanned_sub_dir:
                                for sub_entry in scanned_sub_dir:
                                    if sub_entry.is_file():
                                        print(f"Is File: {sub_entry}")
                                    if sub_entry.is_dir():
                                        print(f"is Directory: {sub_entry}")

        # print(current_file_structure)





main()
