

from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

	# Adds a new node to the graph with no connected edges
    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []

	# Adds an edge to an undirected graph
    def addEdge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

	# Remove the node from the graph by deleting the key-value pair
    def removeNode(self, node):
        if node in self.graph:
            del self.graph[node]
            for key in self.graph:
                self.graph[key] = [(n, w) for n, w in self.graph[key] if n != node]

	# Deletes an edge between the src and dest nodes from the edge list
    def removeEdge(self, src, dest):
        if src in self.graph and dest in self.graph:
            self.graph[src] = [(n, w) for n, w in self.graph[src] if n != dest]
            self.graph[dest] = [(n, w) for n, w in self.graph[dest] if n != src]

	# Returns the degree of a node i.e., how many other nodes it is connected to
    def degree(self, node):
        if node in self.graph:
            return len(self.graph[node])
        else:
            return 0

	# Returns the number of vertices or nodes in a graph
    def getVertexCount(self):
        return self.V

	# Returns the total number of edges in the graph
    def getEdgeCount(self):
        return sum([len(self.graph[node]) for node in self.graph.keys()]) // 2

	# Prints the graph in the format edge: edge list
    def printGraph(self):
        for node in self.graph:
            print(f"Node {node}: {self.graph[node]}")

if __name__ == "__main__":
    # Driver program to test the above functions
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    print("Graph:")
    graph.printGraph()
    print()
    node_to_check = 1
    print(f"Degree of node {node_to_check}:", graph.degree(node_to_check))
    print("Number of vertices:", graph.getVertexCount())
    print()
    graph.removeNode(7)
    print("Graph:")
    graph.printGraph()
    print()
    print(f"Degree of node {node_to_check}:", graph.degree(node_to_check))
    print("Number of vertices:", graph.getVertexCount())

import networkx as nx
import matplotlib.pyplot as plt

def plot_graph(graph):
    G = nx.Graph()

    # Add nodes to the graph
    for node in graph.graph:
        G.add_node(node)

    # Add edges to the graph
    for src in graph.graph:
        for dest, _ in graph.graph[src]:
            G.add_edge(src, dest)

    # Define the layout (e.g., spring_layout, circular_layout, etc.)
    layout = nx.spring_layout(G)

    # Draw the graph
    nx.draw(G, pos=layout, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')
    edge_labels = {tuple([src, dest]): weight for src in graph.graph for dest, weight in graph.graph[src]}
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge_labels, font_color='red')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)

    print("Graph 1:")
    graph.printGraph()
    print()

    plot_graph(graph)

    print("Graph 2:")
    graph.removeNode(7)  # Removing node 7
    graph.printGraph()
    print()
    print(f"Degree of node 1 in Graph 2:", graph.degree(1))

    plot_graph(graph)

