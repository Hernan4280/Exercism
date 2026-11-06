def label(colors):
    c_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    main_value = c_list.index(colors[0]) * 10 + c_list.index(colors[1])
    zeros = c_list.index(colors[2])
    total_value = main_value * (10 ** zeros)
    
    if total_value == 0:
        return "0 ohms"
    elif total_value < 1000:
        return f"{total_value} ohms"
    elif total_value < 1000000:
        value = total_value / 1000
        return f"{int(value) if value == int(value) else value} kiloohms"
    elif total_value < 1000000000:
        value = total_value / 1000000
        return f"{int(value) if value == int(value) else value} megaohms"
    else:
        value = total_value / 1000000000
        return f"{int(value) if value == int(value) else value} gigaohms"
