def square_root(number):
    left = 0
    right = number + 1

    while (left != right - 1):
        middle = (left + right) // 2
        if (middle * middle <= number):
            left = middle
        else:
            right = middle

    return left
