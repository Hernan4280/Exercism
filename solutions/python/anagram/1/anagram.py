def find_anagrams(word: str, candidates: list) -> list:
    target = word.lower()
    target_sorted = sorted(target)
    def filter_words(x):
        if target == x.lower():
            return False
        if target_sorted == sorted(x.lower()):
            return True
        return False
        
    return list(filter(filter_words, candidates))
