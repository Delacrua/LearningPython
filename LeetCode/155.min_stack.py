"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.minimums.append(val if not self.minimums else min(val, self.minimums[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.minimums.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.minimums:
            return None
        return self.minimums[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
