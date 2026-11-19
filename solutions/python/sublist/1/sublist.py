SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif _is_sublist(list_one, list_two):
        return SUBLIST
    elif _is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def _is_sublist(one, two):
    n, m = len(one), len(two)
    if n > m:
        return False
    for i in range((m - n) + 1):
      if one == two[i:len(one) + i]:
          return True
    return False
