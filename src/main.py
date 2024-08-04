import os
import shutil

from copy_static import copy_files_directories
from generate_pages_recursive import generate_pages_recursive

def main():

    source_path = "./static/"
    dest_path = "./public/"
    from_path = "./content/"
    template_path = "./template.html"
    gen_dest_path = "./public/"

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    copy_files_directories(source_path, dest_path)
    generate_pages_recursive(from_path, template_path, gen_dest_path)


if __name__ == "__main__":
    main()
