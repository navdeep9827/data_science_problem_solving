Graph Data Structure and Visualization
This Python script demonstrates the implementation of a graph data structure and its visualization using the NetworkX and Matplotlib libraries. It allows you to create, manipulate, and visualize an undirected graph.

Graph Class
Class Name: Graph
The Graph class is defined with the following methods:

__init__(self, V): Initializes the graph with a given number of vertices.

addNode(self, node): Adds a new node to the graph with no connected edges.

addEdge(self, src, dest, weight): Adds an edge to the undirected graph with a specified weight.

removeNode(self, node): Removes a node from the graph, including all associated edges.

removeEdge(self, src, dest): Removes an edge between two nodes.

degree(self, node): Returns the degree of a given node (number of edges connected to it).

getVertexCount(self): Returns the number of vertices in the graph.

getEdgeCount(self): Returns the total number of edges in the graph.

printGraph(self): Prints the graph in the format Node: Edge List.

Usage:
You can create a Graph object, add nodes and edges, remove nodes and edges, and print various properties of the graph.

Graph Visualization
Libraries Used: NetworkX and Matplotlib
The script also includes a function named plot_graph(graph) that visualizes the graph using NetworkX and Matplotlib.

Usage:
Create a Graph object.
Add nodes and edges.
Use the plot_graph(graph) function to visualize the graph.
Example:
The script demonstrates the creation of a sample graph, adding nodes and edges, and visualizing the graph using the plot_graph function.

Feel free to use this code as a foundation for working with graphs in Python. You can create your graph, add nodes and edges, and visualize the graph using the provided functions.

Please ensure you have the NetworkX and Matplotlib libraries installed to visualize the graph.