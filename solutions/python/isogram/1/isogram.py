def is_isogram(phrase):
    current = [i for i in phrase.lower() if i.isalpha()]
    return len(current) == len(set(current))
