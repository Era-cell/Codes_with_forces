import copy
import math
import time, sys
from collections import defaultdict, deque, Counter
import heapq

import sys
from sortedcontainers import SortedList

"""
  Sparse tables - RANGE QUERIES
  Can be used for - MIN, GCD, MAX
  Cannot be used for - SUM
  Table structure:   0              1        2  3  4 
                  0  e0             e1       e2 e3 e4 | --> covers 2**0 = 1 elements
                  1  f(e0,e1)       f(e1,e2) ...      | --> covers 2**1 = 2 elements
                  2  f(e0,e1,e2,e3) ...               | --> covers 2**2 = 4 elements

                 Stores always inclusive, even in SegTree
"""


# # Implementation for MAX ----------

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# 
# table = [["temp"] * n for _ in range(len(bin(n)[2:]))]
#
# # Stores Inclusive maximum
# for j in range(len(bin(n)[2:])):
#     sl = SortedList()
#     for k in range(2 ** j): sl.add(arr[k])
#     for i in range(n - 2 ** j):
#         table[j][i] = sl[-1]
#         sl.remove(arr[i])
#         sl.add(arr[i + 2 ** j])
#     table[j][n - 2 ** j] = sl[-1]
# print(table)
#
#
# def find_range_max(l, r):
#     j = len(bin(l - r + 1)[2:]) - 1
#     return max(table[j][l], table[j][r - 2 ** j + 1])


# Implementation for GCD -----------

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def find_range_gcd(l, r):
    j = len(bin(l - r + 1)[2:]) - 1
    return gcd(table[j][l], table[j][r - 2 ** j + 1])


n = int(input())
arr = [int(input()) for _ in range(n)]

table = [["temp"] * n for _ in range(len(bin(n)[2:]))]
table[0] = [i for i in arr]

for j in range(1, len(bin(n)[2:])):
    for i in range(n - 2 ** j + 1):
        gcd_ans = gcd(arr[i], arr[i + 1])
        for k in range(2, 2 ** j):
            gcd_ans = gcd(gcd_ans, arr[i + k])
        table[j][i] = gcd_ans

print(find_range_gcd(3, 3))
