"""Solution----------------st the end
green_gold_dog has an array a
 of length n
, and he wants to find a permutation b
 of length n
 such that the number of distinct numbers in the element-wise difference between array a
 and permutation b
 is maximized.

A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in any order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (as 2
 appears twice in the array) and [1,3,4]
 is also not a permutation (as n=3
, but 4
 appears in the array).

The element-wise difference between two arrays a
 and b
 of length n
 is an array c
 of length n
, where ci
 = ai−bi
 (1≤i≤n
).

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤4⋅104
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤4⋅104
).

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
).

It is guaranteed that the sum of n
 over all test cases does not exceed 4⋅104
.

Output
For each test case, output n
 numbers - a suitable permutation b
. If there are multiple solutions, print any of them.
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [[i, ind] for (i, ind) in enumerate(arr)]
    arr.sort(key=lambda x: x[1])
    res = [0 for _ in range(len(arr))]
    for i in arr:
        res[i[0]] = n
        n -= 1


#Test cases:
# 3
# 1
# 100000
# 2
# 1 1
# 3
# 10 3 3
