import numpy as np

# Implementing a Doubly Linked List

# Node class for the individual nodes
class Node:
    # constructor for Node class
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Manager class to link the nodes and manage the overall list
class DoublyLinkedList:
    # constructor for LinkedList class
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Push: Adds a new element at the head of the list
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    # Pop: Deletes the element at the head and returns the value of it
    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        next_node = self.head.next
        if next_node:
            next_node.prev = None
        else:
            self.tail = None
        self.head = next_node
        self.count -= 1
        return data

    # Function to insert a node containing data at some specified position between 1 and x
    def insert(self, data, position):
        # your code here
        if position < 1:
            return "Invalid Position"

        new_node = Node(data)

        if position == 1:
            if not self.head:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            current = self.head
            for _ in range(1, position - 1):
                if current is None:
                    break
                current = current.next
            if current is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node
        self.count += 1

    # Function to delete a node at the specified position between 1 and x
    def delete(self, position):
        # your code here
        if position < 1:
            return "Invalid Position"

        if position == 1:
            if not self.head:
                return
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
        else:
            current = self.head
            for _ in range(1, position):
                if not current:
                    return
                current = current.next
            if current:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
        self.count -= 1

    # Returns the size of the linked list
    def size(self):
        return self.count

    # Return the element at the top of the linked list without removing it
    def top(self):
        if self.head is None:
            return self.head
        return self.head.data

    def isEmpty(self):
        return self.count == 0

    def printIsEmpty(self):
        print("The Linked list is Empty\n") if self.isEmpty() else print(
            "The Linked list is not Empty\n"
        )

    def printList(self):
        current = self.head
        print(current.prev, end=" <-> ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Queue With Tags

class QueueUsingArrays:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = np.empty(self.capacity, dtype=object)
        self.front = 0
        self.rear = 0

    def enqueue(self, data, tag):
      if self.rear == self.capacity:
        self.capacity *= 2
        arr_update = np.empty(shape = self.capacity, dtype = object)
        arr_update[:len(self.queue)] = self.queue
        self.queue = arr_update
      flag = False

      for i in range(self.rear - 1, self.front -1, -1):
        _, tag_in = self.queue[i]
        if tag_in == tag:
          flag = True
          for j in range(self.rear, i, -1):
            self.queue[j+1] = self.queue[j]
          self.queue[i+1] = (data, tag)
          break

      if not flag: #no matching tag in queue yet
        self.queue[self.rear] = (data, tag)
      self.rear += 1

    def dequeue(self):
      if not self.isEmpty():
        pop_val = self.queue[self.front]
        self.front = self.front+1
        return pop_val
      else:
        return None

    def size(self):
        return (self.rear - self.front)

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.capacity

    def printIsEmpty(self):
        print("Queue is Empty\n") if self.isEmpty() else print("Queue is not Empty\n")

    def printQueue(self):
        print("front", end=" ")
        print(list(self.queue[self.front:self.rear]), end=" ")
        print("rear")

    def frontElement(self):
        return self.queue[self.front]

# if __name__ == "__main__":
#   A = QueueUsingArrays(10)
#   A.enqueue(6, 'A')
#   A.enqueue(5, 'B')
#   A.enqueue(7, 'A')
#   A.enqueue(4, 'A')
#   A.printQueue()



