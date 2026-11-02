def steps(number):
    # I validate that the number is not a float, 0, or negative.
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")
        
    current = number
    count = 0
    while current != 1:
        if current & 1:
            current = 3 * current + 1
        else:
            current //= 2
        count += 1
    return count
