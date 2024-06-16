""""
  If equals go, j+1, i+1
  Else:
    j go back until it forms common prefix suffix.
"""


text = input()
pattern = input()

F = [0]
j = 0
for i in range(1, len(pattern)):
    while j > 0 and pattern[j] != pattern[i]:
        j = F[j - 1]
    if pattern[i] == pattern[j]: j += 1
    F.append(j)

res = []
j = 0
for i in range(len(text)):
    if text[i] == pattern[j]:
        j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
            j = F[j - 1]
    else:
        while j > 0 and text[i] != pattern[j]:
            j = F[j - 1]

print(res)
