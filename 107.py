#!/usr/bin/env python

from UnionFind import UnionFind

def GeneralizedPetersenGraph(n,k):
    G = {}
    for i in range(n):
        G[i,True] = (i,False),((i-1)%n,True),((i+1)%n,True)
        G[i,False] = (i,True),((i-k)%n,False),((i+k)%n,False)
    return G

PetersenGraph = GeneralizedPetersenGraph(5,2)

def MinimumSpanningTree(G):
    """
    Return the minimum spanning tree of an undirected graph G.
    G should be represented in such a way that G[u][v] gives the
    length of edge u,v, and G[u][v] should always equal G[v][u].
    The tree is returned as a list of edges.
    """
    
    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    tree = []
    edges = [(G[u][v],u,v) for u in G for v in G[u]]
    edges.sort()
    for W,u,v in edges:
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree        

#mv = 1e8

#mat = [[mv, 16, 12, 21, mv, mv, mv], [16, mv, mv, 17, 20, mv, mv], \
#       [12, mv, mv, 28, mv, 31, mv], [21, 17, 28, mv, 18, 19, 23], \
#       [mv, 20, mv, 18, mv, mv, 11], [mv, mv, 31, 19, mv, mv, 27], \
#       [mv, mv, mv, 23, 11, 27, mv]]

#mst = MinimumSpanningTree(mat)

#print mat

print PetersenGraph
