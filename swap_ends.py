def swap_ends(L, k):
    if type(L) != list or type(k) != int:
        return ([], 0)

    n = len(L)
    if n == 0 or k <= 0 or k > n // 2:
        return (L.copy(), 0)

    new_list = L.copy()
    num_swaps = 0
    i = 0


    while i < k:
        j = n - k + i
        new_list[i], new_list[j] = new_list[j], new_list[i]###tuple unpaking
        num_swaps += 1
        i += 1

    return (new_list, num_swaps)
