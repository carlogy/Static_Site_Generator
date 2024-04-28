import os
import shutil

from textnode import TextNode


def main():
    # node = TextNode("This is a node", "bold", "https://www.boot.dev")
    # print(repr(node))

    static_path = "./static"
    public_path = "./public"



    def copy_directory(path):
        public_path = "./public"
        if os.path.exists(public_path):
            shutil.rmtree(public_path)
        os.mkdir(public_path)
        if not os.path.exists(path):
            raise IsADirectoryError("The directory does not exist, or system permissions for this directory are not granted.\n Run ls -l (dir_path) to view permission.\nTo modify use command chomd.")
        folder_structure = {}

        if os.path.exists(path):

            static_tree = os.walk(path, topdown=True)

            list_structure = list(static_tree)

            for dir, dir_names, file_names in list_structure:
                for child_dir in dir_names:
                    if dir_names in os.listdir(public_path):
                        continue
                    if len(dir.removeprefix("./").split("/")) == 1:
                        os.mkdir(os.path.join(public_path, child_dir))
                    else:
                        parent_dir = dir.removeprefix("./static")
                        path_to_create = f"{public_path}{parent_dir}/{child_dir}"
                        os.mkdir(path_to_create)
                        print(os.path.exists(path_to_create))
                for file in file_names:
                    if len(dir.removeprefix("./").split("/")) == 1:
                        shutil.copy(os.path.join(dir,file), os.path.join(public_path))
                    else:
                        parent_dir = dir.removeprefix("./static")
                        path_to_create = f"{public_path}{parent_dir}/{file}"
                        shutil.copy(os.path.join(dir,file), path_to_create)

    copy_directory(static_path)

main()
