Dijkstra's Algorithm and Minimum Spanning Tree
This Python script demonstrates the implementation of Dijkstra's algorithm for finding the shortest path and Prim's algorithm for finding the Minimum Spanning Tree (MST) in a graph. The code defines two main functions:

Dijkstra's Algorithm
Function: dijkstra(graph, src, dest=None)
This function calculates the shortest distance from a given source vertex to all other vertices in a graph. It uses Dijkstra's algorithm for this purpose.

graph: The graph object to perform Dijkstra's algorithm on.
src: The source vertex to calculate the distances from.
dest: An optional parameter to calculate the shortest distance to a specific destination vertex. If not provided, it returns the distances to all vertices.
Minimum Spanning Tree (Prim's Algorithm)
Function: primMST(graph, src)
This function finds the Minimum Spanning Tree (MST) of a given graph using Prim's algorithm. It returns the total cost of traversing the MST.

graph: The graph object to calculate the MST for.
src: The source vertex from which the MST is calculated.
Example Usage:
The script demonstrates how to create a graph, add nodes and edges, and then perform Dijkstra's algorithm and calculate the MST using the functions mentioned above.

You can use this code as a foundation for working with graphs and finding the shortest paths and MST in Python.

Example:
The script provides an example graph and demonstrates how to use Dijkstra's algorithm and calculate the MST. It prints the results to the console.

Ensure you have the provided Graph class (from the LE7.py file) for this code to work. The Graph class is used for representing the graph data structure.