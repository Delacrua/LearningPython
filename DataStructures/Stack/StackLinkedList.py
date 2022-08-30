"""
Implementation of stack using a singly linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "<-"
            cur = cur.next
        return out[:-2] if out[:-2] else 'EMPTY STACK'

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        print('pushed item: ', value)

    def pop(self):
        if self.is_empty():
            return "this stack is empty"
        popped_element = self.head.next
        self.head.next = self.head.next.next  # None
        self.size -= 1
        return popped_element.value

    def peek(self):
        if self.is_empty():
            return "this stack is empty"
        return self.head.next.value

    def clear_stack(self):
        self.head = Node('head')
        self.size = 0


a = Stack()
a.push('a')
a.push('b')
a.push('c')
print(a)
print(a.is_empty())
print(a.pop())
print(a)
print(a.peek())
print(a.is_empty())
a.clear_stack()
print(a)
print(a.is_empty())
