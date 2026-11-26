import re

def decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""

    parts: list[str] = []
    for match in re.finditer(r"\d+.|\s+|[a-zA-Z]+", encoded_text):
        if match.group(0)[0].isdigit():
            count = int(match.group(0)[:-1])
            char = match.group(0)[-1]
            parts.append(char * count)
        else:
            parts.append(match.group(0))

    return "".join(parts)

def encode(text: str) -> str:
    if not text:
        return ""

    parts: list[str] = []
    for match in re.finditer(r"(.)\1*", text):
        count = len(match.group(0))
        parts.append(f"{count}{match.group(0)[0]}" if count > 1 else match.group(0)[0])

    return "".join(parts)
