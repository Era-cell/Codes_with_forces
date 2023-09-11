

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [[i, ind] for (i, ind) in enumerate(arr)]
    arr.sort(key=lambda x: x[1])
    res = [0 for _ in range(len(arr))]
    for i in arr:
        res[i[0]] = n
        n -= 1