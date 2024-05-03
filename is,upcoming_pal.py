def upcoming_pal(s):
    """ considering s isn't a pal """
    
def is_pal(s):
    i, j= 0, len(s)-1
    while i<j:
        if s[i]!=s[j]: return False
        i, j = i+1, j-1
    return True
  
