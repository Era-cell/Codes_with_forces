def next_pal(s):
    center = int(math.ceil(len(s)/2.0)-1)
    temp = center
    if len(s)%2==1:
        if int(s[center])<9:
            return s[:center]+str(int(s[center])+1)+s[center+1:]
        else:
            center-=1
    while center>-1 and s[center]=="9":
        center-=1
    if len(s)%2==0:
        if center==-1: return "1"+"0"*(len(s)-1)+"1"
        else:
            return s[:center] + str(int(s[center])+1) + "0"*2*(temp-center) + (s[:center] + str(int(s[center])+1))[::-1]
    else:
        temp-=1
        if center==-1: return "1"+"0"*(len(s)-1)+"1"
        else:
            return s[:center] + str(int(s[center])+1) + "0"*(temp-center) + "0" + "0"*(temp-center) + (s[:center] + str(int(s[center])+1))[::-1]
