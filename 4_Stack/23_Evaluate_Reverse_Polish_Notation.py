"""
Problem: Evaluate Reverse Polish Notation
Link: https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150
Category: Stack
Created on: 6/17/2025

Approach:
- Used a stack to append the numbers
- Popped the top of the stack when an operator appeared, and performed said operation
"""
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                pop = stack.pop()
                stack.append(stack.pop() - pop)
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                pop = stack.pop()
                stack.append(int(stack.pop() / pop))
            else:
                stack.append(int(tokens[i]))
        return stack[0]

test = Solution()
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))