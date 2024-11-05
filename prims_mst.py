import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst():
    # Input number of vertices
    n = int(input("Enter the number of vertices: "))

    # Input the adjacency matrix
    print("Enter the adjacency matrix (use 0 or None for no edge):")
    adj_matrix = []
    for i in range(n):
        row = list(map(lambda x: None if x.lower() == 'none' else int(x), input().split()))
        adj_matrix.append(row)

    # Initialize the graph representation for visualization
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):  # To avoid duplicate edges in undirected graph
            if adj_matrix[i][j] is not None and adj_matrix[i][j] > 0:
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Prim's MST algorithm using min-heap
    visited = [False] * n
    min_heap = [(0, 0, -1)]  # Start from vertex 0, with -1 as a dummy parent
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        if parent != -1:  # If not the initial dummy parent
            mst_edges.append((parent, u, weight))

        for v in range(n):
            if adj_matrix[u][v] is not None and not visited[v]:
                heapq.heappush(min_heap, (adj_matrix[u][v], v, u))

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
    plt.title("Minimum Spanning Tree (Prim's Algorithm)")
    plt.show()

prim_mst()
