# Binary Exponentiaton
def pow(a, n, m):
    if n == 1:
        return a
    elif n % 2 == 1:
        return (pow(a, n // 2, m)**2)%m * a % m
    else:
        return pow(a, n // 2, m)**2 % m

  # TODO: Matrix Exponentiation
