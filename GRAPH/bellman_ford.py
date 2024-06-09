import sys

""""
Applies for directed graph. 
Not applicable for undirected graphs because:
 consider 0->1 is -2 it means 1->0 is also -2, so there is a -ve cycle
 Bellman ford doesn't apply for -ve cycle containing graphs
"""

n = int(input("No of vertices: "))

adj = defaultdict(list)
source = int(input("Enter source: "))
result = [sys.maxsize] * n
result[source] = 0
edges = []
for _ in range(int(input("Enter no of edges: "))):
    _from, to, weight = list(map(int, input().split(" ")))
    edges.append((_from, to, weight))
    if _from == source:
        result[to] = weight

for _ in range(n):
    for _from, _to, weight in edges:
        result[_to] = min(result[_to], result[_from] + weight)
temp = result
for _from, _to, weight in edges:
    result[_to] = min(result[_to], result[_from] + weight)

if temp != result:
    print("Negative cycle exists")
else:
    print(result)
