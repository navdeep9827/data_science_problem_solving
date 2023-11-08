class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def build_expression_tree(expression):
    # Function to check if a token is an operator
    def is_operator(token):
        return token in "+-*/"

    # Determine the precedence of an operator
    def precedence(token):
        if token in "+-":
            return 1
        elif token in "*/":
            return 2
        return 0

    # Convert infix expression to a list of tokens
    tokens = []
    current_token = ""
    for char in expression:
        if char.isnumeric() or char == ".":
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char.strip():
                tokens.append(char)
    if current_token:
        tokens.append(current_token)

    # Convert infix expression to postfix notation
    postfix = []
    stack = []
    for token in tokens:
        if token.isnumeric():
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()  # Pop the opening parenthesis
        elif is_operator(token):
            while stack and is_operator(stack[-1]) and precedence(token) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    # Build the expression tree
    stack = []
    for token in postfix:
        if token.isnumeric():
            stack.append(Node(int(token)))
        elif is_operator(token):
            right = stack.pop()
            left = stack.pop()
            new_node = Node(token)
            new_node.left = left
            new_node.right = right
            stack.append(new_node)

    return stack[0]  # The root of the expression tree

def evaluate_expression_tree(root):
    if not root:
        return None

    if not root.left and not root.right:
        return int(root.val)  # Ensure the result is an integer

    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    if root.val == '+':
        return left_val + right_val
    elif root.val == '-':
        return left_val - right_val
    elif root.val == '*':
        return left_val * right_val
    elif root.val == '/':
        if right_val == 0:
            return None
        return left_val / right_val
    elif root.val == '//':
        if right_val == 0:
            return None
        return left_val / right_val



