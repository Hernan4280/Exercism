SUFFIXES = {1: "st", 2: "nd", 3: "rd"}

def line_up(name, number):
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = SUFFIXES.get(number % 10, "th")
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
