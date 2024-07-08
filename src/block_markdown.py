# function to convert raw markdown text to blocks of markdown text

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    stripped_blocks = []
    for i in split_blocks:
        if i == "":
            continue
        stripped_blocks.append(i.strip())
    return stripped_blocks
