import sys
from LE7 import *

def dijkstra(graph, src, dest=None):
    if src not in graph.graph:
        return None

    distances = {}
    visited = set()
    for node in graph.graph:
        distances[node] = sys.maxsize

    distances[src] = 0

    while visited != set(graph.graph):
        current_node = None
        min_distance = sys.maxsize
        for node in graph.graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        visited.add(current_node)

        for neighbor, weight in graph.graph[current_node]:
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

    if dest is None:
        return distances
    else:
        return distances[dest] if distances[dest] != sys.maxsize else None

def primMST(graph, src):
    if src not in graph.graph:
        return None

    mst_cost = 0
    key = {}
    parent = {}
    min_heap = [(0, src)]

    for node in graph.graph:
        key[node] = sys.maxsize
        parent[node] = None

    key[src] = 0

    while min_heap:
        weight, u = min_heap.pop(0)
        if weight > key[u]:
            continue

        mst_cost += weight

        for v, w in graph.graph[u]:
            if w < key[v]:
                key[v] = w
                parent[v] = u
                min_heap.append((w, v))

    return mst_cost

# Helper function to print the distance dictionary received from dijkstra()
def printArr(dist):
    print("Vertex Distance")
    for i in dist:
        print(f"{i} {dist[i]}")

# Create the graph using adjacency lists
graph = Graph()
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 3)
graph.addEdge(1, 2, 5)
graph.addEdge(1, 7, 11)
graph.addEdge(7, 6, 1)
graph.addEdge(7, 8, 7)
graph.addEdge(2, 3, 12)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 8)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 13)
graph.addEdge(6, 8, 6)

source_vertex = 0

print("Graph:")
graph.printGraph()
print(f"Source vertex: {source_vertex}")

dijkstra_result = dijkstra(graph, source_vertex)
print(dijkstra_result)
printArr(dijkstra_result)

# Calculate the shortest distance from 0 to 8
shortest_distance = dijkstra_result[8]
print(f"Shortest distance from {source_vertex} to 8: {shortest_distance}")

# Calculate the cost of MST traversal from vertex 1
mst_cost = primMST(graph, 1)
print(f"Cost of MST traversal from vertex 1: {mst_cost}")









if __name__ == "__main__":
    # Driver program to test the above functions
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 3)
    graph.addEdge(1, 2, 5)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 12)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 8)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 13)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    print("Graph:")
    graph.printGraph()
    print()
    src = 0
    dist = dijkstra(graph, src)
    print(f"Source vertex: {src}")
    print(dist)
    print()
    printArr(dist)
    print()
    dest = 8
    print(f"Shortest distance from {src} to {dest}: {dijkstra(graph, 0, dest)}")
    print()
    print(f"Cost of MST traversal from vertex {1}: {primMST(graph, 1)}")