def value(colors):
    return int("".join(map(str, [get_digit(colors[i]) for i in range(2)])))

def get_digit(color):
    list_colors = [
        "black", 
        "brown", 
        "red", 
        "orange", 
        "yellow", 
        "green", 
        "blue", 
        "violet", 
        "grey", 
        "white"
]
    return list_colors.index(color)
