import math
def factors(n) : 
    res = []
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i != i) : 
                res.append(n/i)
            res.append(i)
        i = i + 1
    return res
