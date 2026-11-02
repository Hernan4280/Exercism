def is_pangram(sentence):
    current = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in current:
            return False
    return True
