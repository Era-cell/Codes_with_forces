text = input()
pattern = input()

zarr = [0]

for i in range(1, len(pattern)):
    count = 0
    j = 0
    while j < i and pattern[i + j] == pattern[j]: j += 1
    zarr.append(j)

# aabxdaabxaaby
# aabx
text = pattern + text
# aabxaabxdaabxaaby
res = copy.deepcopy(zarr)
l = len(pattern)
while l < len(text):
    r = l
    # simply go until it matches but stop if mathcing l itself
    while r < len(text) and text[r] == text[r - l] and r - l < l:
        r += 1
    res.append(r - l)
    for i in range(l + 1, r):
        # This means when there is "aab" you say 4, i.e, aabx matches
        if res[i - l] + i >= r: break
        res.append(res[i - l])
    l = len(res)

print(res)
