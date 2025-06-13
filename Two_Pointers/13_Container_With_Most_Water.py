"""
Problem: Container With Most Water
Link: https://neetcode.io/problems/max-water-container?list=neetcode150
Category: Two Pointers
Created on: 6/12/2025

Approach:
-
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
                count = 0
                while heights[l + count] == heights[r - count]:
                    count += 1
                    if heights[l + count] > heights[r - count]:
                        l += 1
                    elif heights[l + count] < heights[r - count]:
                        r -= 1
                    else:
                        count += 1
        return maxarea
test = Solution()
print(test.maxArea([2,2,2]))