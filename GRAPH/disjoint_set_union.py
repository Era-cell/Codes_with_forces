""""
DSU(Disjoint Set Union): 
  logN update, logN find.
  1 -- 2
  |       4 -- 5
  3    
  [{1,2,3}, {4,5}]
Finding and updating edges the components belonging to same group in running graph
"""


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        # You need size only because to reduce the height of graph
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
        # remember this recur with present parent
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]


n = int(input("No of vertices: "))
edges = []
dsu = DSU(n)
for _ in range(int(input("Enter no of edges: "))):
    _from, to, weight = map(int, input().strip().split())
    edges.append((_from, to, weight))
    dsu.update(_from, to)

edges.sort(key=lambda x: x[2])

for i in range(n):
    print(dsu.find_parent(i))
print(dsu.size[dsu.find_parent(3)])
