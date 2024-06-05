def isprime(n):
    i = 6
    if n < 4:
        return False
    square_root = math.sqrt(n)
    while i < square_root:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    if square_root % 6 == 0 and n % square_root - 1 == 0:
        return False
    return True
