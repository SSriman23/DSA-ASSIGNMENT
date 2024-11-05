# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:41:35 2024

@author: ssrim
"""

import heapq 
import networkx as nx 
import matplotlib.pyplot as plt 
  
def dijkstra(graph, source): 
    distances = {node: float('infinity') for node in graph} 
    distances[source] = 0 
    previous_nodes = {node: None for node in graph} 
    priority_queue = [(0, source)] 
     
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
         
        if current_distance > distances[current_node]: 
            continue 
         
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                previous_nodes[neighbor] = current_node 
                heapq.heappush(priority_queue, (distance, neighbor)) 
     
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
        v, weight = map(int, input(f"Enter destination vertex and weight for edge from {i}:").split()) 
        graph[i][v] = weight 
  
source = int(input("Enter the source vertex: ")) 
distances, previous_nodes = dijkstra(graph, source) 
  
# Output distances and paths 
print("Shortest distances and paths from source:") 
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
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", 
font_size=10, font_weight="bold") 
edge_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 
plt.title("Graph Representation (Dijkstra’s Algorithm)") 
plt.show() 