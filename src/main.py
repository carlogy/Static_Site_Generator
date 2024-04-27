import os
import shutil

from textnode import TextNode


def main():
    # node = TextNode("This is a node", "bold", "https://www.boot.dev")
    # print(repr(node))

    static_path = "./static"
    public_path = "./public"



    def copy_directory(path):
        if not os.path.exists(path):
            raise IsADirectoryError("The directory does not exist, or system permissions for this directory are not granted.\n Run ls -l (dir_path) to view permission.\nTo modify use command chomd.")
        folder_structure = {}

        if os.path.exists(path):
            print(f"The path exists! {path}")

            with os.scandir(path) as scanned_directory:
                print(type(scanned_directory))


                list_of_scanned_dir = sorted(scanned_directory, key=lambda entry: entry.is_dir(),)

                current_public_path = public_path
                for entry in list_of_scanned_dir:
                    if entry.is_file():
                        print(f"{entry.name} is a valid file\nLocated in: {entry.path}\n")
                        shutil.copy(entry.path, current_public_path)
                    if entry.is_dir():
                        print(f"{entry.name} is a directory\nIt's path is: {entry.path}")
                        with os.scandir(public_path) as child_directory:
                            if entry.name not in list(child_directory):
                                print("The directory doesn't exists!")

                                os.mkdir(f"{current_public_path}/{entry.name}")
                                current_public_path = f"{current_public_path}/{entry.name}"
                                copy_directory(entry.path)

    # copy_directory(static_path)

main()
