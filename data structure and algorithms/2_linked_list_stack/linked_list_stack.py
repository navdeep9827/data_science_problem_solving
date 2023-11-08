# Lab Exercise - 2

# Implementing Stacks Linked Lists

# Node class for the individual nodes
class Node:

    # constructor for Node class
    def __init__(self, data):
        self.data=data
        self.next= None

# Manager class to link the nodes and manage the overall list
class LinkedListStack:

    # constructor for LinkedListStack class
    def __init__(self):
        self.head= None
        self.stack_size= 0


    # Push: Adds a new element at the back of the list
    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.stack_size += 1


    # Pop: Deletes the element at the last and returns the value of it
    def pop(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.stack_size -= 1
            return data
        else:
            return None


    # Returns the size of the stack
    def size(self):
        return self.stack_size


    # Return the element at the top of the stack without removing it
    def top(self):
        return self.head.data if self.head else None



    # Return true is stack is empty, False if not
    def isEmpty(self):
        return self.stack_size == 0


    def printIsEmpty(self):
        print("\nStack is Empty\n") if self.isEmpty() else print("\nStack is not Empty\n")


    # Reverses the stack
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def printStack(self):
        temp = self.head
        print("\nThe Stack created is as follows: \n")
        while(temp):
            print (temp.data, end=" ")
            temp = temp.next


# # Create a stack
# stack = LinkedListStack()
#
# # Test 1: Check if the stack is empty
# print("Test 1:")
# stack.printIsEmpty()
#
# # Test 2: Push elements onto the stack and check the size
# print("\nTest 2:")
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("Size of the stack:", stack.size())
#
# # Test 3: Check if the stack is empty after pushing elements
# print("\nTest 3:")
# stack.printIsEmpty()
#
# # Test 4: Peek at the top element
# print("\nTest 4:")
# print("Top element:", stack.top())
#
# # Test 5: Pop elements from the stack
# print("\nTest 5:")
# print("Popped element:", stack.pop())
# print("Popped element:", stack.pop())
# print("Popped element:", stack.pop())
# print("Popped element:", stack.pop())  # Should return None as the stack is empty
#
# # Test 6: Check if the stack is empty after popping all elements
# print("\nTest 6:")
# stack.printIsEmpty()
#
# # Test 7: Reverse the stack
# print("\nTest 7:")
# stack.push(4)
# stack.push(5)
# stack.push(6)
# print("Original stack:")
# stack.printStack()
# stack.reverseList()
# print("Reversed stack:")
# stack.printStack()
