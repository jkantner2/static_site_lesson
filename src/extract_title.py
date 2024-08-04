def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.lstrip("# ")
