"""
Problem: Valid Parentheses
Link: https://neetcode.io/problems/validate-parentheses?list=neetcode150
Category: Stack
Created on: 6/16/2025

Approach:
- Used stack to store any open parentheses
- True if stack was empty, otherwise false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pdict = {'(': ')', '[': ']', '{': '}'}
        for p in s:
            if p in pdict:
                stack.append(p)
            elif p in pdict.values():
                if not stack:
                    return False
                if p == pdict[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack

test = Solution()
print(test.isValid("[()]"))