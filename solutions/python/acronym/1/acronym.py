import re
def abbreviate(words: str) -> str:
    clean = re.sub(r"[_-]", " " , words)
    return "".join([word[0].upper() for word in clean.split()])
