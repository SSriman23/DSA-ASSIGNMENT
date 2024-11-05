# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:14:05 2024

@author: ssrim
"""

import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_mst():
    # Input number of vertices
    n = int(input("Enter the number of vertices: "))

    # Input the adjacency matrix
    print("Enter the adjacency matrix (use 0 or None for no edge):")
    adj_matrix = []
    for i in range(n):
        row = list(map(lambda x: None if x.lower() == 'none' else int(x), input().split()))
        adj_matrix.append(row)

    # Initialize the graph for visualization and create edge list
    edges = []
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicate edges in undirected graph
            if adj_matrix[i][j] is not None and adj_matrix[i][j] > 0:
                edges.append((adj_matrix[i][j], i, j))
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Sort edges by weight for Kruskal's algorithm
    edges.sort()
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    # Kruskal's MST algorithm
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    # Display the MST cost and plot the graph
    print("Minimum Spanning Tree cost:", mst_cost)
    print("Edges in MST:")
    for u, v, weight in mst_edges:
        print(f"Edge ({u}, {v}) with weight {weight}")

    # Plotting the original graph and MST
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Original Graph")

    # Display the MST with edges only from mst_edges
    MST = nx.Graph()
    for u, v, weight in mst_edges:
        MST.add_edge(u, v, weight=weight)
    
    plt.subplot(122)
    nx.draw(MST, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (Kruskal's Algorithm)")
    plt.show()

kruskal_mst()
