# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:52:32 2024

@author: ssrim
"""
import networkx as nx 
import matplotlib.pyplot as plt 
from collections import defaultdict 

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

# DFS function using recursion and a visited set 
def dfs(graph, start, visited=None, traversal_order=None): 
    if visited is None: 
        visited = set() 
    if traversal_order is None: 
        traversal_order = [] 

    visited.add(start)              # Mark node as visited 
    traversal_order.append(start)    # Add to traversal order 

    # Recurse into unvisited neighbors 
    for neighbor, weight in graph[start]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited, traversal_order) 

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

# Main code to run DFS and plot the graph 
graph = create_graph_from_matrix() 
start_node = int(input("Enter the starting node (0-indexed): ")) 
  
# Run DFS 
dfs_order = dfs(graph, start_node) 
print("DFS Traversal Order:", dfs_order) 

# Plot the graph 
plot_graph(graph) 
