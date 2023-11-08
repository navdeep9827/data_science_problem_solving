
README for Stack Data Structures and Infix to Postfix Conversion

This repository contains Python code for implementing and using three different stack data structures: ArrayStack, DoublingArrayStack, and LinkedListStack. Additionally, the code provides a function for converting infix expressions to postfix notation.

Stack Data Structures

The code includes three distinct stack data structure implementations:

ArrayStack

ArrayStack is an implementation of a stack using an array with a fixed size. It can dynamically expand its size when needed.
The stack supports essential operations such as push, pop, top, size, and checking if it is isEmpty.
This implementation allows elements of any data type.

DoublingArrayStack

DoublingArrayStack is similar to ArrayStack but with a dynamic resizing strategy.
The stack doubles its size when it becomes full and halves its size when it is less than one-fourth full.
It also supports standard stack operations like push, pop, top, size, and isEmpty.
This implementation allows elements of any data type.

LinkedListStack

LinkedListStack is an implementation of a stack using a singly linked list.
It provides push, pop, top, size, and isEmpty operations.
It can efficiently reverse the order of elements in the stack.

Infix to Postfix Conversion

The code includes a function called infix_to_postfix that converts infix expressions to postfix notation. This function uses one of the stack implementations to facilitate the conversion. The code follows standard rules for operator precedence and handles parentheses.

How to Use

To use the stack data structures or the infix to postfix conversion function, follow these steps:

Import the necessary classes and functions from the code into your Python script.

Create an instance of one of the stack data structures: ArrayStack, DoublingArrayStack, or LinkedListStack.

Use the stack to perform various stack operations such as pushing elements onto the stack, popping elements from the stack, checking the top element, checking if the stack is empty, and getting the size of the stack.

Utilize the infix_to_postfix function to convert infix expressions to postfix notation. Pass the infix expression and the stack instance as arguments to the function