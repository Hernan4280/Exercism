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


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    if list:
        return list.index(list[-1]) + 1
    return 0


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    accumulator = initial
    for li in list:
        accumulator = function(accumulator, li)
    return int(accumulator)


def foldr(function, list, initial):
    accumulator = initial
    for li in list[::-1]:
        accumulator = function(accumulator, li)
    return accumulator if isinstance(accumulator, str) else int(accumulator)


def reverse(list):
    return list[::-1]
