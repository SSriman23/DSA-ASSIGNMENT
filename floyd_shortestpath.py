# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:45:18 2024

@author: ssrim
"""

import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt 
  
def floyd_warshall(graph, num_vertices): 
    # Initialize the distance matrix with infinity and next_node matrix for path reconstruction 
    dist = np.full((num_vertices, num_vertices), float('inf')) 
    next_node = [[None] * num_vertices for _ in range(num_vertices)] 
     
    # Set the distance from each vertex to itself as 0 
    for i in range(num_vertices): 
        dist[i][i] = 0 
     
    # Fill initial distances based on direct edges in the graph 
    for u in graph: 
        for v, weight in graph[u].items(): 
            dist[u][v] = weight 
            next_node[u][v] = v 
     
    # Floyd-Warshall algorithm to compute all pairs shortest paths 
    for k in range(num_vertices): 
        for i in range(num_vertices): 
            for j in range(num_vertices): 
                if dist[i][j] > dist[i][k] + dist[k][j]: 
                    dist[i][j] = dist[i][k] + dist[k][j] 
                    next_node[i][j] = next_node[i][k] 
                     
    return dist, next_node 
  
def get_path(next_node, start, end): 
    if next_node[start][end] is None: 
        return [] 
    path = [start] 
    while start != end: 
        start = next_node[start][end] 
        path.append(start) 
    return path 
  
# Input and Execution 
num_vertices = int(input("Enter the number of vertices: ")) 
graph = {i: {} for i in range(num_vertices)} 
  
for i in range(num_vertices): 
    edges = int(input(f"Enter number of edges from vertex {i}: ")) 
    for _ in range(edges): 
        v, weight = map(int, input(f"Enter destination vertex and weight for edge from {i}: ").split()) 
        graph[i][v] = weight 
  
# Run Floyd-Warshall to get distances and paths 
distances, next_node = floyd_warshall(graph, num_vertices) 
  
# Output Distance Matrix 
print("\nShortest Path Distance Matrix:") 
print("     ", end="") 
for i in range(num_vertices): 
    print(f"{i:6}", end=" ") 
print() 
for i in range(num_vertices): 
    print(f"{i:2} ", end="") 
    for j in range(num_vertices): 
        if distances[i][j] == float('inf'): 
            print(f"{'inf':6}", end=" ") 
        else: 
            print(f"{distances[i][j]:6.1f}", end=" ") 
    print() 
  
# Output detailed paths 
print("\nAll-pairs shortest path distances and paths:") 
for i in range(num_vertices): 
    for j in range(num_vertices): 
        if distances[i][j] == float('inf'): 
            print(f"No path from {i} to {j}") 
        else: 
            path = get_path(next_node, i, j) 
            print(f"Shortest path from {i} to {j}: Distance = {distances[i][j]}, Path = {path}") 
  
# Plotting the Graph 
G = nx.DiGraph() 
for u in graph: 
    for v, weight in graph[u].items(): 
        G.add_edge(u, v, weight=weight) 
  
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightcoral", 
font_size=10, font_weight="bold") 
edge_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 
plt.title("Graph Representation (Floyd-Warshall Algorithm)") 
plt.show()