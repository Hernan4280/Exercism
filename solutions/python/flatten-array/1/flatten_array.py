def flatten(iterable: list) -> list:
    flatened = []
    for item in iterable:
        if item == None:
            continue
        if isinstance(item, list):
            flatened.extend(flatten(item))
        else:
            flatened.append(item)
    return flatened
