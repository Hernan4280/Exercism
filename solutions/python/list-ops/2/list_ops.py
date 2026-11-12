def append(list1, list2):
    if isinstance(list2, int):
        list1[len(list1):] = [list2]
    else:
        list1[len(list1):] = [i for i in list2]
    return list1


def concat(lists):
    flattened = []
    for li in lists:
        if isinstance(li, list):
            flattened += li
        else:
            append(flattened, li)
    return flattened


def filter(function, lista):
    return [i for i in lista if function(i)]


def length(lista):
    if lista:
        return lista.index(lista[-1]) + 1
    return 0


def map(function, lista):
    return [function(i) for i in lista]


def foldl(function, lista, initial):
    accumulator = initial
    for li in lista:
        accumulator = function(accumulator, li)
    return int(accumulator)


def foldr(function, lista, initial):
    accumulator = initial
    for li in lista[::-1]:
        accumulator = function(accumulator, li)
    return accumulator if isinstance(accumulator, str) else int(accumulator)


def reverse(lista):
    return lista[::-1]
