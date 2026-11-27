import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def prime(number: int) -> int:
    if number < 1:
        raise ValueError('there is no zeroth prime')

    count: int = 0
    candidate: int = 1
    while count < number:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate
