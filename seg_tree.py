import sys

# Exists: SUM, Segment Sum - (pref, suff, ans, sum)
# For these change backtracked results in `tree`
# MAX SegTree:
class SegTree:

    def __init__(self, arr):
        self.arr = arr
        self.tree = [-1] * (4 * len(arr))

    def build(self, node, st, end):
        if st == end:
            self.tree[node] = self.arr[st]
        else:
            mid = (st + end) // 2
            self.build(2 * node, st, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, node, st, end, i, x):
        if st == end:
            self.tree[node] = x
        else:
            mid = (st + end) // 2
            if i <= mid:
                self.update(node * 2, st, mid, i, x)
            else:
                self.update(node * 2 + 1, mid + 1, end, i, x)
            self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, node, st, end, qs, qe):
        if qs <= st and end <= qe:
            return self.tree[node]
        elif qe < st or end < qs:
            # we return unknown value which is safer like:
            return -sys.maxsize
        else:
            mid = (st + end) // 2
            return max(self.query(node * 2, st, mid, qs, qe), self.query(node * 2 + 1, mid + 1, end, qs, qe))

# ------------------- USAGE ---------------------------
arr = [1, 2, 3, 4, 5, 3, 4, 9, 111]
segT = SegTree(arr)

segT.build(1, 0, len(arr) - 1)
print(segT.tree)

# segT.update(1, 0, len(arr) - 1, 4, 22)
# print(segT.query(1, 0, len(arr) - 1, 6, 8))

# ------------------- Question 6 -----------------------
# Question 6: find index which is the beginning of the number above given number, when the array is DYNAMIC
# queries: (1, i, x) update index i with x
# queries: (2, x) find the least index having val>=x
# eg: 5, ans: 4

# update
segT.update(1, 0, len(arr) - 1, 4, 22)

# query
# what you can get is the range query i.e, from (0, 7) i.e, (qs, qe) where qs<qe
print(segT.query(1, 0, len(arr) - 1, 6, 8))

print(segT.tree)
# eg: 20, answer: 4
# only thing is we can binary search on SegTree
x = 20
l, r = 0, len(arr) - 1
while l < r:
    mid = (l + r) // 2
    if segT.query(1, 0, len(arr) - 1, 0, mid) >= x:
        r = mid
    else:
        l = mid + 1

print(l)
