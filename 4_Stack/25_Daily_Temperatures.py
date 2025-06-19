"""
Problem: Daily Temperatures
Link: https://neetcode.io/problems/daily-temperatures?list=neetcode150
Category: Stack
Created on: 6/18/2025

Approach:
- Used stack and appended every i into it
- Only popped it if a larger number appeared in a future iteration
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop = stack.pop()
                res[pop] = i - pop
            stack.append(i)
        return res

test = Solution()
print(test.dailyTemperatures([22,21,20]))
