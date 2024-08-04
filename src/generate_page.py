from markdown_to_htmlnode import markdown_to_htmlnode
from htmlnode import *
from extract_title import extract_title
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from: {from_path} to {dest_path}, using {template_path}")
    with open(from_path) as f:
        from_path_markdown = f.read()

    with open(template_path) as f:
        template_path_read_data = f.read()

    title = extract_title(from_path_markdown)
    htmlnode = markdown_to_htmlnode(from_path_markdown)
    html = htmlnode.to_html()

    template_path_read_data = template_path_read_data.replace("{{ Title }}", title)
    template_path_read_data = template_path_read_data.replace("{{ Content }}", html)

    req_dirs = os.path.dirname(dest_path)
    if not os.path.exists(req_dirs):
        os.mkdirs(req_dirs)
    with open(dest_path, "x") as f:
        f.write(template_path_read_data)
