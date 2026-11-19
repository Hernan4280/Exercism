def egg_count(display_value: int) -> int:
    binary = bin(display_value)[2:]
    return list(binary).count("1")
