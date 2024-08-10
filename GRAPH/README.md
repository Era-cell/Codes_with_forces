# Graph

##  Minimum cost path from

### One node to all other nodes/ other node without -ve weights: Dijkstra's - *O( E * logV )*

### One node to all other nodes even with -ve weights: Bellman ford - O( V * E )

### All nodes to all other node: Floyd Warshall - O( V ** 3 )

### All nodes to all other node: Johnson's algorithm = Bellmanford(on new vertice 0 weight) + Deduce relative weight + Dijkstra's on all vertices - O( V * E * logV )

Note: Floyd warshall may be equivalent or even better than Johnson's if number of edges are V*(V-1)/2

## Minimum cost spanning tree

- Kruskal's algorithm = Sort weights + Include edges not forming cycles(using DSU) - O( E * logE )

## Disjoint Set Union

## Topological sorting

- By using DFS
- By using BFS(indegree): Kahn's algorithm

## Euler's path

- Hierholzer's thorem = Go to as depth as possible using DFS

## Number of regions in a planar graph

- Euler found out that: Vertices + Regions = Edges + 2


## Properties

+ M ^ X, Mij gives number of paths of length X from i to j


