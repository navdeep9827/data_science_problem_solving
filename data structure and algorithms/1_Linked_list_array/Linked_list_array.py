class StackArrays:
    def __init__(self):
        # Initialize the stack using an array (list)
        self.stack = []

    def push(self, element):
        # Add an element to the top of the stack
        self.stack.append(element)

    def pop(self):
        # Remove the topmost element in the stack and return it
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def size(self):
        # Return the size of the stack (the number of elements in the list)
        return len(self.stack)

    def top(self):
        # Return the element at the top of the stack without removing it
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise IndexError("Top on an empty stack")

    def isEmpty(self):
        # Return True if the stack is empty, False if not
        return len(self.stack) == 0

# Testing the StackArrays class
# if __name__ == "__main__":
#     stack = StackArrays()
#
#     # Pushing elements onto the stack
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#
#     # Checking the top element
#     print("Top element:", stack.top())  # Output: Top element: 3
#
#     # Popping elements from the stack
#     popped_item = stack.pop()
#     print("Popped item:", popped_item)  # Output: Popped item: 3
#
#     # Checking if the stack is empty
#     print("Is stack empty?", stack.isEmpty())  # Output: Is stack empty? False
#
#     # Checking the size of the stack
#     print("Stack size:", stack.size())  # Output: Stack size: 2


