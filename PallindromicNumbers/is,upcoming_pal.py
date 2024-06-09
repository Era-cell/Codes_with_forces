def is_pal(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i, j = i + 1, j - 1
    return True


def upcoming_pal(s):
    """ considering upcoming of s is s itself is that's a pallindrome"""
    if is_pal(s): return s
    center = int(math.ceil(len(s) / 2.0) - 1)

    temp = center if len(s) % 2 == 0 else center - 1
    while temp > -1 and s[temp] == s[len(s) - temp - 1]:
        temp -= 1

    left, right = temp, len(s) - temp - 1
    if int(s[left]) > int(s[right]):
        return s[:left + 1] + s[left + 1: right] + s[:left + 1][::-1]
    else:
        if len(s) % 2 == 1 and s[center] != "9": return s[:center] + str(int(s[center]) + 1) + s[:center][::-1]
        while s[center] == "9": center -= 1
        left, right = center, len(s) - center - 1
        return s[:left] + str(int(s[left]) + 1) + ("0" * (right - left - 1)) + (s[:left] + str(int(s[left]) + 1))[::-1]
  
