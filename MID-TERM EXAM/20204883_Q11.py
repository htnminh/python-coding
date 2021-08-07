def is_increasing(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            print('NO')
            return None
    print('YES')
    return None
            