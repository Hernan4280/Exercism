def is_armstrong_number(number: int) -> bool:
    splited = [int(i) for i in str(number)]
    return sum([num ** len(splited) for num in splited]) == number
