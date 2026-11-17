import re
def translate(text: str) -> str:
    
    return " ".join(_translate_word(w) for w in text.split())

def _translate_word(word: str) -> str:

    if re.match(r"^(?:[aeiou]|xr|yt)", word):
        return word + "ay"

    rule_3 = re.match(r"^([^aeiou\s]*qu)(\S*)$", word)
    if rule_3:
        return rule_3.group(2) + rule_3.group(1) + "ay"

    rule_4 = re.match(r"^([^aeiouy\s]+)(y\S*)$", word)
    if rule_4:
        return rule_4.group(2) + rule_4.group(1) + "ay"

    rule_2 = re.match(r"^([^aeiou\s]+)(\S*)$", word)
    if rule_2:
        return rule_2.group(2) + rule_2.group(1) + "ay"

    return word + "ay"