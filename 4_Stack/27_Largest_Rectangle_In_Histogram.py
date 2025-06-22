"""
Problem: Largest Rectangle In Histogram
Link: https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150
Category: Stack
Created on: 6/21/2025

Approach:
-
"""
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        area = []
        while l < r:
            rectangle = r - l + 1 * min(heights[l], heights[r])
            area.append(rectangle)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

test = Solution()
print(test.largestRectangleArea([7,1,7,2,2,4]))