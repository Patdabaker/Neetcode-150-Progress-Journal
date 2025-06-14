"""
Problem: Container With Most Water
Link: https://neetcode.io/problems/max-water-container?list=neetcode150
Category: Two Pointers
Created on: 6/12/2025

Approach:
- Use two pointer approach with pointers on opposite sides
- Took the max area of the min heights of the pointers and the distance between them
- Moved the pointer that had a lesser height
- If equal, moved the pointer whose next point had a greater height
"""
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        maxarea = 0
        while l < r:
            maxarea = max(maxarea, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                if heights[l + 1] > heights[r - 1]:
                    l += 1
                elif heights[l + 1] < heights[r - 1]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
        return maxarea
test = Solution()
print(test.maxArea([1,7,2,5,4,7,3,6]))