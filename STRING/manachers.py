"""
  Longest Pallindromic substring
  Handled even length pallindromes too using "#"
"""
# Why the fuck do you think we use "#"? To cover even length pals
text = "".join("#" + i for i in s) + "#"
# abaxabaxab
# acbbca
j = 0
x = 0
res = [1]

longest = 0
for i in range(1, len(text)):

    # Mirror place to check for the result, `j` will be right
    if j < i or i + (res[x - (j - x) + (j - i)] // 2) == j:
        if j < i:
            j = i + 1
        else:
            j += 1
        x = i

        # compare and expand `j`
        while x - (j - x) > -1 and j < len(text) and text[j] == text[x - (j - x)]:
            j += 1
        j -= 1
        if j - x > longest:
            resultant_center = x
            longest = j - x
        res.append(1 + 2 * (j - x))
    else:

        # min bcz previous has matched more, but now the limit is less
        res.append(min(1 + 2 * (j - i), res[x - (j - x) + (j - i)]))
        
resultant_string = ""
for i in text[resultant_center - longest:resultant_center + longest + 1]:
    if i != "#": resultant_string += i
print(resultant_string, longest, res)
