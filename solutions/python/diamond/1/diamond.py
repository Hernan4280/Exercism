def rows(letter: str) -> list[str]:
    n = ord(letter) - ord('A')
    current_rows = []

    for i in range(2 * n + 1):
        distance_to_center = abs(n - i)
        step = n - distance_to_center
        char = chr(ord('A') + step)
        extremes = ' ' * distance_to_center

        if step == 0:
            row = f"{extremes}{char}{extremes}"
        else:
            internal_spaces = ' ' * (2 * step - 1)
            row = f"{extremes}{char}{internal_spaces}{char}{extremes}"

        current_rows.append(row)

    return current_rows
