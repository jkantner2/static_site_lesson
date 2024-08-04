import os
import pathlib
from generate_page import generate_page


def generate_pages_recursive(from_path, template_path, dest_dir_path):
    from_path = pathlib.Path(from_path)
    dir_contents = os.listdir(from_path)
    for file in dir_contents:
        file_path = os.path.join(from_path, file)
        if os.path.isfile(file_path):
            dest_file_html = file.replace(".md", ".html")
            to_path = os.path.join(dest_dir_path, dest_file_html)
            generate_page(file_path, template_path, to_path)
            continue
        dest_dir_path = os.path.join(dest_dir_path, file)
        generate_pages_recursive(file_path, template_path, dest_dir_path)


if __name__ == '__main__':
    generate_pages_recursive()
