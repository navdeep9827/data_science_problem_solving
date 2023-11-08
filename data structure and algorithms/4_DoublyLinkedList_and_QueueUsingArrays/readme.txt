Python Classes: DoublyLinkedList and QueueUsingArrays
This repository contains two Python classes:

DoublyLinkedList: This class implements a doubly linked list that supports basic operations such as push, pop, insert, delete, size, top, isEmpty, and printing the list.

QueueUsingArrays: This class implements a queue using arrays, with the ability to enqueue and dequeue elements, check if the queue is empty or full, and more.

Class: DoublyLinkedList
Usage
To use the DoublyLinkedList class, you can create an instance of this class to work with doubly linked lists. The class provides various methods to manipulate the list.

Methods
push(data): Adds a new element at the head of the list.
pop(): Deletes the element at the head and returns its value.
insert(data, position): Inserts a node containing data at a specified position.
delete(position): Deletes a node at the specified position.
size(): Returns the current size of the linked list.
top(): Returns the element at the head of the linked list without removing it.
isEmpty(): Checks if the linked list is empty.
printList(): Prints the elements of the linked list.
Class: QueueUsingArrays
Usage
The QueueUsingArrays class implements a queue using arrays. You can create an instance of this class to work with queues and perform enqueue and dequeue operations.

Methods
enqueue(data, tag): Enqueues an element with an associated tag.
dequeue(): Dequeues an element from the front of the queue.
size(): Returns the current size of the queue.
isEmpty(): Checks if the queue is empty.
isFull(): Checks if the queue is full.
printQueue(): Prints the elements in the queue.
frontElement(): Returns the element at the front of the queue.