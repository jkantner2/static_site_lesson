from htmlnode import *
from textnode import *
from block_markdown import *
from inline_markdown import *


def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_nodes.append(to_htmlnode_from_block_type(block, block_type))
    for block_node in block_nodes:
        if block_node.tag == "pre":
            continue
        if block_node.tag == "ol" or block_node.tag == "ul":
            block_node.children = create_list_items(block_node.value)
            block_node.value = None
            continue
        children = text_to_children(block_node.value)
        block_node.children = children
        block_node.value = None
    return HTMLNode("div", None, block_nodes)
        

# MUST ADDRESS does block heading text need to be stipped from block value???

def to_htmlnode_from_block_type(block, block_type):
    if block_type == block_type_quote:
        return HTMLNode("blockquote", block.lstrip().lstrip(">").lstrip())
    
    # Does this need to have second HTMLNode? can we just create children w/ code tag from block
    if block_type == block_type_code:
         return HTMLNode("pre", None, [LeafNode("code", block.strip().strip("`"))])

    if block_type == block_type_heading:
        for level in range(1, 6):
            if block.startswith("#" * level + " "):
                content = block.lstrip("#").lstrip()
                return HTMLNode(f"h{level}", content)

    if block_type == block_type_ulist:
        return HTMLNode("ul", block)

    if block_type == block_type_olist:
        return HTMLNode("ol", block)

    if block_type == block_type_paragraph:
        return HTMLNode("p", block.lstrip())


def text_to_children(text):
    print("-" * 20)
    print(f"Text: {text}")
    print("-" * 20)
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(textnode.text_node_to_html_node())
    return htmlnodes


def create_list_items(block):
    items = block.split("\n")
    li_nodes = []
    for item in items:
        li_nodes.append(HTMLNode("li", item.lstrip().lstrip("* ").lstrip("- ").lstrip("0123456789. ")))
    return li_nodes

