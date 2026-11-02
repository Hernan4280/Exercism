import sys
def square(number):
    #Number of grains on a given square.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    #Total number of grains on the chessboard.
    return (square(64) * 2) - 1
