import re

# function to convert raw markdown text to blocks of markdown text

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    stripped_blocks = []
    for i in split_blocks:
        if i == "":
            continue
        stripped_blocks.append(i.strip())
    return stripped_blocks

# function to determine block type

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def block_to_block_type(block):
    split_leading_characters = block.split(" ", 1)
    leading_characters = split_leading_characters[0]
    trailing_characters = split_leading_characters[1]
    heading_check = re.findall(r"#{1,6}", leading_characters)
    split_newline = block.split("\n")

    if leading_characters in heading_check and len(trailing_characters) > 0:
        return block_type_heading
    
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    
    valid_line_counter = 0
    for line in split_newline:
        if line[0] ==  ">":
            valid_line_counter += 1
    if valid_line_counter ==  len(split_newline):
        valid_line_counter = 0
        return block_type_quote

    valid_unordered_list_counter = 0
    for line in split_newline:
        if line[:2] == "* " or line[:2] == "- ":
            valid_line_counter += 1
    if valid_line_counter == len(split_newline):
        valid_line_counter = 0
        return block_type_unordered_list

    valid_ordered_list_counter = 0
    for line in split_newline:
        starting_character = line[:3]
        match = re.findall(r"\d\. ", starting_character)
        if match != [] and starting_character == match[0]:
            valid_ordered_list_counter += 1
    if valid_ordered_list_counter == len(split_newline):
        valid_line_counter = 0
        return block_type_ordered_list

    return block_type_paragraph

