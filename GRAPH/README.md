#  Minimum cost path from

## One node to all other nodes/ other node without -ve weights:

### Dijkstra's
### O( E * logV )

## One node to all other nodes even with -ve weights:

### Bellmanford
### O( V * E )

## All nodes to all other nodes

### Johnson's algorithm = Bellmanford(on new vertice 0 weight) + Deduce relative weight + Dijkstra's on all vertices
### O( V * E * logV )

# Minimum cost spanning tree

### Kruskal's algorithm = Sort weights + Include edges not forming cycles(using DSU)
### O( E * logE )

# Disjoint Set Union
