""""
Kruskal's MST using DSU:
So, complexity is: O(N * logN)
"""


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def update(self, node1, node2):
        p1 = self.find_parent(node1)
        p2 = self.find_parent(node2)
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]

    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]


n = int(input("No of vertices: "))
edges = []
dsu = DSU(n)
for _ in range(int(input("Enter no of edges: "))):
    _from, to, weight = map(int, input().strip().split())
    edges.append((_from, to, weight))

edges.sort(key=lambda x: x[2])

res = []
weight = 0
for src, dest, w in edges:
    if dsu.find_parent(src) != dsu.find_parent(dest):
        res.append((src, dest))
        dsu.update(src, dest)
        weight += w

print(res, weight)
