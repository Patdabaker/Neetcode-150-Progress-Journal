"""
Problem: Evaluate Reverse Polish Notation
Link: https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150
Category: Stack
Created on: 6/17/2025

Approach:
-
"""
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                pop = stack.pop()
                stack.append(stack.pop() - pop)
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                pop = stack.pop()
                stack.append(int(pop // stack.pop()))
        return stack[0]

test = Solution()
print(test.evalRPN(["1","2","+","3","*","4","-"]))