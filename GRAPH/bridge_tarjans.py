"""
Bridge is an edge which increases the number of components in a graph
For undirected graph:
Complexity: O( E )
"""

from collections import defaultdict

n = int(input("Number of edges: "))

adj = defaultdict(list)
edges = int(input("Enter no of edges: "))
for _ in range(edges):
    # input edges from -> to
    frm, to = list(map(int, input().split(" ")))
    adj[frm].append(to)
    adj[to].append(frm)

discovery_time = [-1] * n
least_discovery_time = [-1] * n
visited = [0] * n
time = -1


def recur(curr, parent=-1):
    if visited[curr]: return [discovery_time[curr], []]
    global time
    time += 1
    discovery_time[curr], least_discovery_time[curr] = time, time
    visited[curr] = 1
    res = []
    for node in adj[curr]:
        if node != parent:
            least_time, r = recur(node, curr)
            # if I am(i.e, node) connected to someone who is already visited, I am connected. Thats great
            least_discovery_time[curr] = min(least_discovery_time[curr], least_time)
            res += r
            if least_discovery_time[curr] != least_discovery_time[node]: res.append((curr, node))
    return [least_discovery_time[curr], res]


print(recur(0)[1])
