C_LIST = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

TOLERANCE_BAND = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%",
                  "green": "0.5%", "brown": "1%", "red": "2%",
                  "gold": "5%", "silver": "10%"}


def resistor_label(colors):
    n = len(colors)

    if n == 1:
        return "0 ohms"

    band_value = TOLERANCE_BAND[colors[-1]]
    total_value = get_value(colors, n)

    if total_value < 1000:
        return f"{total_value} ohms ±{band_value}"
    elif total_value < 1000000:
        value = total_value / 1000
        unit = "kiloohms"
    elif total_value < 1000000000:
        value = total_value / 1000000
        unit = "megaohms"
    else:
        value = total_value / 1000000000
        unit = "gigaohms"

    value = int(value) if value == int(value) else value
    return f"{value} {unit} ±{band_value}"


def get_value(colors, n):
    if n == 4:
        digit_colors, multiplier = colors[:2], colors[2]
    else:  # n == 5
        digit_colors, multiplier = colors[:3], colors[3]

    main_value = int("".join(str(C_LIST.index(c)) for c in digit_colors))
    return main_value * 10 ** C_LIST.index(multiplier)
