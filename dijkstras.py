res = [0] * n
visited = [0] * n
visited[0] = 1
q = [(y, x) for x, y in adj[0]]
heapq.heapify(q)
while q:
    p = heapq.heappop(q)
    if visited[p[1]]: continue
    visited[p[1]] = 1
    res[p[1]] = p[0]
    for node, val in adj[p[1]]:
        heapq.heappush(q, (p[0] + val, node))


print(res)
