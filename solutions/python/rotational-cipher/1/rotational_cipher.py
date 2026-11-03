import string
def rotate(text, key):
    result = []
    for char in text:
        if char.islower():
            result.append(rot_char(string.ascii_lowercase, char, key))
        elif char.isupper():
            result.append(rot_char(string.ascii_uppercase, char, key))
        else:
            result.append(char)
    return "".join(result)

            
def rot_char(alpha, char, key):
    idx = alpha.index(char)
    return alpha[(idx + key) % 26]
