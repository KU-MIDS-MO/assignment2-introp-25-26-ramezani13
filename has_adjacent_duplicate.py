def has_adjacent_duplicate(L):
    if type(L) != list:
        return False
    if len(L) < 2:
        return False

    i = 0
    while i < len(L) - 1:
        if L[i] == L[i + 1]:
            return True
        i = i + 1
    return False
