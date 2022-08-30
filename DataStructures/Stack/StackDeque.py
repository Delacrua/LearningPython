"""
Implementation of stack using deque collection
"""
from collections import deque


def create_stack():
    stack = deque()
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    return stack.pop()


def peek(stack):
    if is_empty(stack):
        return "stack is empty"
    return stack[-1]


def clear_stack(stack):
    stack.clear()


a = create_stack()
push(a, 'a')
push(a, 'b')
print(is_empty(a))
pop(a)
print(peek(a))
print(is_empty(a))
clear_stack(a)
print(is_empty(a))
