import numpy as np
import time
from collections import deque
# import matplotlib.pyplot as plt

class ArrayStack:

    def __init__(self, size):
        self.max_size = size
        self.stack = np.empty(size, dtype=object)
        self.top_index = -1

    def push(self, element):
        if self.top_index < self.max_size - 1:
            self.top_index += 1
            self.stack[self.top_index] = element
        else:
            self.stack = np.concatenate((self.stack,np.empty(1,dtype=object)),axis=0)
            self.top_index += 1
            self.stack[self.top_index] = element

    def pop(self):
        if not self.isEmpty():
            element = self.stack[self.top_index]
            self.top_index -= 1
            return element
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    def size(self):
        return self.top_index + 1

    def top(self):
        if not self.isEmpty():
            return self.stack[self.top_index]
        else:
            print("Stack is empty. Cannot get the top element.")
            return None

    def isEmpty(self):
        return self.top_index == -1

    def printIsEmpty(self):
        print("\nStack is Empty\n") if self.isEmpty() else print("\nStack is not Empty\n")

    def printStack(self):
        print(self.stack[:self.top_index + 1])

class DoublingArrayStack:

    def __init__(self, size):
        self.max_size = 0
        self.capacity = size
        self.stack = np.empty(size, dtype=object)

    def double_check(self):
        if self.max_size == self.capacity:
            self._resize(2 * self.capacity)

    def push(self, element):
        self.double_check()
        self.stack[self.max_size] = element
        self.max_size += 1

    def pop(self):
        if not self.isEmpty():
            self.max_size -= 1
            element = self.stack[self.max_size]
            self.stack[self.max_size] = None
            if self.max_size > 0 and self.max_size == self.capacity // 4:
                self._resize(self.capacity // 2)
            return element
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    def size(self):
        return self.max_size

    def top(self):
        if not self.isEmpty():
            return self.stack[self.max_size - 1]
        else:
            print("Stack is empty. Cannot get top element.")
            return None

    def isEmpty(self):
        return self.max_size == 0

    def _resize(self, new_capacity):
        new_stack = np.empty(new_capacity, dtype=object)
        for i in range(self.max_size):
            new_stack[i] = self.stack[i]
        self.capacity = new_capacity
        self.stack = new_stack

    def printIsEmpty(self):
        print("\nStack is Empty\n") if self.isEmpty() else print("\nStack is not Empty\n")

    def printStack(self):
        print(self.stack[:self.max_size])

# Node class for the individual nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Manager class to link the nodes and manage the overall list
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.max_size = 0

    # Push: Adds a new element at the back of the list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.max_size += 1

    # Pop: Deletes the element at the last and returns the value of it
    def pop(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.max_size -= 1
            return data
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    # Returns the size of the stack
    def size(self):
        return self.max_size

    # Return the element at the top of the stack without removing it
    def top(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("Stack is empty. Cannot get top element.")
            return None

    # Return true if the stack is empty, False if not
    def isEmpty(self):
        return self.max_size == 0

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

    # Print data stored in the stack
    def printStack(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def infix_to_postfix(expression, stack):
    # Define a dictionary to store operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Helper function to check if a character is an operator
    def is_operator(char):
        return char in "+-*/^"

    # Helper function to compare operator precedence
    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    postfix = []

    for char in expression:
        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == '(':  # Left parenthesis
            stack.push(char)
        elif char == ')':  # Right parenthesis
            while not stack.isEmpty() and stack.top() != '(':
                postfix.append(stack.pop())
            if not stack.isEmpty() and stack.top() != '(':
                return "Invalid expression"
            else:
                stack.pop()
        elif is_operator(char):  # Operator
            while (not stack.isEmpty() and stack.top() != '(' and
                    has_higher_precedence(stack.top(), char)):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return ''.join(postfix)


# if __name__ == '__main__':
#     input_expression = 'a+b*c'

#     s1 = ArrayStack(len(input_expression))
#     s2 = DoublingArrayStack(len(input_expression))
#     s3 = LinkedListStack()

#     output_expression_1 = infix_to_postfix(input_expression, s1)
#     output_expression_2 = infix_to_postfix(input_expression, s2)
#     output_expression_3 = infix_to_postfix(input_expression, s3)

#     print(output_expression_1)