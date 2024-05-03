def upcoming_pal(s):
    """ considering s isn't a pal """
    i = 0
    while s[i] == s[len(s) - i - 1]:
        i += 1
    if int(s[i]) < int(s[len(s) - i - 1]):
        return s[:i] + str(int(s[i]) + 1) + ((len(s) - i - 2) - i) * "0" + str(int(s[i]) + 1) + s[len(s) - i:]
    else:
        return s[:i] + str(int(s[i])) + ((len(s) - i - 2) - i) * "0" + str(int(s[i])) + s[len(s) - i:]

def is_pal(s):
    i, j= 0, len(s)-1
    while i<j:
        if s[i]!=s[j]: return False
        i, j = i+1, j-1
    return True
  
