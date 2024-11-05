# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:44:11 2024

@author: ssrim
"""

from collections import deque 
import networkx as nx 
import matplotlib.pyplot as plt 
  
def topological_sort(graph): 
    indegree = {node: 0 for node in graph} 
    for u in graph: 
        for v in graph[u]: 
            indegree[v] += 1 
     
    queue = deque([node for node in graph if indegree[node] == 0]) 
    order = [] 
     
    while queue: 
        node = queue.popleft() 
        order.append(node) 
        for neighbor in graph[node]: 
            indegree[neighbor] -= 1 
            if indegree[neighbor] == 0: 
                queue.append(neighbor) 
     
    return order 
  
def shortest_path_dag(graph, source): 
    order = topological_sort(graph) 
    distances = {node: float('infinity') for node in graph} 
    previous_nodes = {node: None for node in graph} 
    distances[source] = 0 
     
    for node in order: 
        if distances[node] != float('infinity'): 
            for neighbor, weight in graph[node].items(): 
                if distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
                    previous_nodes[neighbor] = node 
     
    return distances, previous_nodes 
  
def get_path(previous_nodes, target): 
    path = [] 
    while target is not None: 
        path.append(target) 
        target = previous_nodes[target] 
    return path[::-1] 
  
# Input and Execution 
num_vertices = int(input("Enter the number of vertices: ")) 
graph = {i: {} for i in range(num_vertices)} 
  
for i in range(num_vertices): 
    edges = int(input(f"Enter number of edges from vertex {i}: ")) 
    for _ in range(edges): 
        v, weight = map(int, input(f"Enter destination vertex and weight for edge from {i}: ").split()) 
        graph[i][v] = weight 
  
source = int(input("Enter the source vertex: ")) 
distances, previous_nodes = shortest_path_dag(graph, source) 
  
# Output distances and paths 
print("Shortest distances and paths from source in DAG:") 
for target in graph: 
    if distances[target] == float('infinity'): 
        print(f"Vertex {target} is not reachable from source.") 
    else: 
        path = get_path(previous_nodes, target) 
        print(f"Vertex {target}: Distance = {distances[target]}, Path = {path}") 
  
# Plotting the Graph 
G = nx.DiGraph() 
for u in graph: 
    for v, weight in graph[u].items(): 
        G.add_edge(u, v, weight=weight) 
  
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightgreen", 
font_size=10, font_weight="bold") 
edge_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 
plt.title("DAG Representation (Dynamic Programming for DAG)") 
plt.show() 