def is_beautiful(k):
    a = 1
    while k - 3*a > 0:
        if (k - 3*a) % 5 == 0:
            return 'YES'
        a += 1
    return 'NO'