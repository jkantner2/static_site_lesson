from htmlnode import *
from textnode import *
from block_markdown import *
from inline_markdown import *


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        node = block_to_htmlnode(block)
        nodes.append(node)
    return ParentNode("div", nodes, None)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(textnode.text_node_to_html_node())
    return htmlnodes


def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return block_to_paragraph(block)
    if block_type == block_type_heading:
        return block_type_heading(block)
    if block_type == block_type_quote:
        return block_to_quote(block)
    if block_type == block_type_code:
        return block_to_code(block)
    if block_type == block_type_ulist:
        return block_to_ulist(block)
    if block_type == block_type_olist:
        return block_to_olist(block)
    raise ValueError("Invalid block type")


def block_to_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def block_to_heading(block):
    hashes = block.split(" ", 1)
    lines = hashes[1].lstrip().split("\n")
    paragraph = " ".join(lines)
    level = 0
    for hash in hashes[0]:
        level += 1
    if level < 1:
        raise ValueError("Invalid heading level")
    children = text_to_children(paragraph)
    return ParentNode(f"h{level}", children)


def block_to_quote(block):
    if not block.startswith(">"):
        raise ValueError("Invalid quote block")
    lines = block.lstrip(">").lstrip().split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("blockquote", children)


def block_to_code(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    lines = block.strip("`")
    children = text_to_children(lines)
    return ParentNode("pre", [ParentNode("code", children)])


def block_to_ulist(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def block_to_olist(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


if __name__ == '__main__':
    main()
