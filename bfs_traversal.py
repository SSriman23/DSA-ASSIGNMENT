# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:50:18 2024

@author: ssrim
"""

import networkx as nx 
import matplotlib.pyplot as plt 
from collections import deque, defaultdict 

# Function to create a weighted directed graph from an adjacency matrix 

def create_graph_from_matrix(): 
    num_nodes = int(input("Enter the number of nodes in the graph: ")) 
    print("Enter the adjacency matrix (use 0 or None for no direct edge):") 
     
    matrix = [] 
    for i in range(num_nodes): 
        row = input(f"Row {i+1} (separate values with spaces): ").split() 
        matrix.append([None if val == 'None' or val == '0' else int(val) for val in row]) 
     
    graph = defaultdict(list) 
    for i in range(num_nodes): 
        for j in range(num_nodes): 
            if matrix[i][j] is not None: 
                graph[i].append((j, matrix[i][j])) 

    return graph 

# BFS function using a visited set instead of color marking 
def bfs(graph, start): 
    visited = set()            # Track visited nodes 
    queue = deque([start])      # Queue for BFS 
    traversal_order = []        # To store the BFS traversal order 

    while queue: 
        node = queue.popleft() 
        if node not in visited: 
            visited.add(node)           # Mark as visited 
            traversal_order.append(node) # Add to traversal order 
            
            # Enqueue all unvisited neighbors 
            for neighbor, weight in graph[node]: 
                if neighbor not in visited: 
                    queue.append(neighbor) 

    return traversal_order 

# Function to plot the graph 
def plot_graph(graph): 
    G = nx.DiGraph() 
    for node in graph: 
        for neighbor, weight in graph[node]: 
            G.add_edge(node, neighbor, weight=weight) 
     
    pos = nx.spring_layout(G) 
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)} 
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrows=True) 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red') 
    plt.title("Weighted Directed Graph") 
    plt.show() 
  
# Main code to run BFS and plot the graph 
graph = create_graph_from_matrix() 
start_node = int(input("Enter the starting node (0-indexed): ")) 

# Run BFS 
bfs_order = bfs(graph, start_node) 
print("BFS Traversal Order:", bfs_order) 

# Plot the graph 
plot_graph(graph) 