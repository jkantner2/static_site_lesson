import os
import shutil

from copy_static import copy_files_directories


def main():

    source_path = "./static/"
    dest_path = "./public/"

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    copy_files_directories(source_path, dest_path)


if __name__ == "__main__":
    main()
