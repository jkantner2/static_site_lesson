import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        image_tups = extract_markdown_images(old_node.text)
        text_list = []
        text = old_node.text
        if image_tups == []:
            new_nodes.append(old_node)
            continue
        for i in range(len(image_tups)):
            sections = text.split(f"![{image_tups[i][0]}]({image_tups[i][1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if i == len(image_tups) - 1:
                text_list.extend(sections)
            else:
                text_list.append(sections[0])
                text = sections[1]
            text_list = [i for i in text_list if i != ""]
        for i in range(len(text_list)):
            new_nodes.append(TextNode(text_list[i], text_type_text))
            if i == 0 or i <= len(image_tups) - 1:
                new_nodes.append(TextNode(image_tups[i][0], text_type_image, image_tups[i][1]))
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        link_tups = extract_markdown_links(old_node.text)
        text_list = []
        text = old_node.text
        if link_tups == []:
            new_nodes.append(old_node)
            continue
        for i in range(len(link_tups)):
            sections = text.split(f"[{link_tups[i][0]}]({link_tups[i][1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if i == len(link_tups) - 1:
                text_list.extend(sections)
            else:
                text_list.append(sections[0])
                text = sections[1]
        text_list = [i for i in text_list if i != ""]
        for i in range(len(text_list)):
            new_nodes.append(TextNode(text_list[i], text_type_text))
            if i == 0 or i <= len(link_tups) - 1:
                new_nodes.append(TextNode(link_tups[i][0], text_type_link, link_tups[i][1]))
    
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

