def is_pangram(sentence):
    current = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return all(char in current for char in alphabet)
