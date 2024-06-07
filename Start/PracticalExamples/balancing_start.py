# Example file for Programming Foundations: Algorithms by Joe Marini
# Use a stack to see if a programming statement is balanced


def is_balanced(str):
    # TODO: Your code goes here
    stack = []
    for char in str:
        if char in ['(','[','{']:
            stack.append(char)
        if char in [')',']','}']:
            if len(stack) == 0: return False
            poping = stack.pop()
            if poping == '(' and char != ')': return False
            if poping == '[' and char != ']': return False
            if poping == '{' and char != '}': return False
    
    return len(stack) == 0

test_statements = [
    "print('Hello World!')",
    "a(x[i]) == b(x[i])",
    "{c for c in a(x)}",
    "Hello!)",
    "(This is not [balanced)",
    "{{{[[(())]}}",
    "(",
    "}"
]

for statement in test_statements:
    print(f'{statement} balanced: {is_balanced(statement)}')
