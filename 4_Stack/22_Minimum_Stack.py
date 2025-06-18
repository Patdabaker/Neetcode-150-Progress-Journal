"""
Problem: Minimum Stack
Link: https://neetcode.io/problems/minimum-stack?list=neetcode150
Category: Stack
Created on: 6/17/2025

Approach:
- Brute forced it all
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

test = MinStack()
test.push(1)
test.push(2)
test.push(0)
print(test.getMin())
test.pop()
print(test.top())
print(test.getMin())