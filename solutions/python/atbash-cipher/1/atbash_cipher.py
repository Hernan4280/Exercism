import re

PLAIN  = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

def _clean(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def _substitution(text, src, dst):
    table = str.maketrans(src, dst)
    return text.translate(table)

def encode(plain_text):
    cleaned = _clean(plain_text)
    result  = _substitution(cleaned, PLAIN, CIPHER)
    return " ".join(result[i:i+5] for i in range(0, len(result), 5))

def decode(ciphered_text):
    cleaned = _clean(ciphered_text)
    return _substitution(cleaned, CIPHER, PLAIN)
