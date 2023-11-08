Python Class: Binary Search Tree (BST) Node
This Python class, BST_Node, represents the nodes of a Binary Search Tree (BST). A BST is a tree data structure where each node has at most two children, referred to as the left child and the right child. It satisfies the BST property, which ensures that for each node:

All nodes in the left subtree have keys less than the node's key.
All nodes in the right subtree have keys greater than the node's key.
Class: BST_Node
Usage
You can use the BST_Node class to create and manipulate a BST. It provides the following methods and functionalities:

insert(key): Inserts a new node with the specified key into the BST.
delete(key): Deletes the node with the specified key from the BST.
min_val(): Returns the minimum value in the BST.
max_val(): Returns the maximum value in the BST.
find(lkpkey): Searches for a key in the BST and returns True if found, False otherwise.
PrintTree(): Prints the BST in an in-order traversal.