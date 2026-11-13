def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    multiples = {m for m in multiples if m > 0}
    return sum({
        item
        for value in multiples
        for item in range(value, limit, value)
    })
