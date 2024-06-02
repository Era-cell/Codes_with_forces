import sys


# SUM tree
class LazySegTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [-1] * (4 * len(arr))
        self.lazy = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, st, end):
        if st == end:
            self.tree[node] = self.arr[st]
        else:
            mid = (st + end) // 2
            self.build(node * 2, st, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, st, end, qs, qe):
        if self.lazy[node]:
            self.tree[node] += (end - st + 1) * self.lazy[node]
            if 2 * node <= 2 * len(self.arr): self.lazy[2 * node] += self.lazy[node]
            if 2 * node + 1 <= 2 * len(self.arr): self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        # 1st have dynamic variable in comparison: qs, qe doesnt change here
        if end < qs or st > qe:
            return 0
        if qs <= st and end <= qe:
            return self.tree[node]
        mid = (st + end) // 2
        return self.query(node * 2, st, mid, qs, qe) + self.query(node * 2 + 1, mid + 1, end, qs, qe)

    def update(self, node, st, end, qs, qe, val):
        if self.lazy[node]:
            self.tree[node] += (end - st + 1) * self.lazy[node]
            if 2 * node <= 2 * len(self.arr): self.lazy[2 * node] += self.lazy[node]
            if 2 * node + 1 <= 2 * len(self.arr): self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        if qe < st or end < qs:
            return
        if qs <= st and end <= qe:
            self.tree[node] += (end - st + 1) * val
            if 2 * node <= 2 * len(self.arr): self.lazy[2 * node] += val
            if 2 * node + 1 <= 2 * len(self.arr): self.lazy[2 * node + 1] += val
            return
        mid = (st + end) // 2
        self.update(node * 2, st, mid, qs, qe, val)
        self.update(node * 2 + 1, mid + 1, end, qs, qe, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = LazySegTree(arr)
print(tree.tree)
print(tree.query(1, 0, len(arr) - 1, 2, 5))
tree.update(1, 0, len(arr) - 1, 2, 5, 10)
print(tree.tree)
print(tree.query(1, 0, len(arr) - 1, 4, 7))
print(tree.tree)
