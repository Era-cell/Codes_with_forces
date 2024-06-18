"""
Consider "bbaacaa", 
Answer: "aabbaac" is the lexicographically smallest - after rotation
-- can Also use Booth's algorithm

Pseudo Algo:


ret = one which is our present choice
l = length of present common prefix
idx = present candidate

for all the characters:
(compare) cp = alphabet of chosen - alphabet of candidate
if cp==0: l++
elif cp<0(left is smaller):
  idx = ret+l; l=0
else:(right is smaller)
  ret = max(ret+l+1, idx); idx=ret+1; l=0;

"""
