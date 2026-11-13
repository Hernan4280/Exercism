def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    current_data = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            key = letter.lower()
            current_data[key] = score
    return current_data
