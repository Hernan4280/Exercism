def factors(value: int) -> list[int]:
    divisors = []
    divisor = 2

    while divisor * divisor <= value:
        while value % divisor == 0:
            divisors.append(divisor)
            value //= divisor
        divisor += 1

    if value > 1:
        divisors.append(value)

    return divisors
