import os
import shutil


def copy_directory(path):
    public_path = "./public"
    os.mkdir(public_path)
    if not os.path.exists(path):
        raise IsADirectoryError("The directory does not exist, or system permissions for this directory are not granted.\n Run ls -l (dir_path) to view permission.\nTo modify use command chomd.")

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
            for file in file_names:
                if len(dir.removeprefix("./").split("/")) == 1:
                    shutil.copy(os.path.join(dir,file), os.path.join(public_path))
                else:
                    parent_dir = dir.removeprefix("./static")
                    path_to_create = f"{public_path}{parent_dir}/{file}"
                    shutil.copy(os.path.join(dir,file), path_to_create)
