"""
Problem: Trapping Rain Water
Link: https://neetcode.io/problems/trapping-rain-water?list=neetcode150
Category: Two Pointers
Created on: 6/13/2025

Approach:
- Used two pointer starting from the beginning for each
- Calculated space in between bars while subtracting space taken in between
- Added all the space to the max area
- Returned 0 if length was less than 3 since it's impossible for there to be space in between
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, 0
        maxarea = 0
        between = 0
        area = 0
        if len(height) < 3:
            return 0
        while l < len(height):
            while height[l] == 0:
                l += 1
            while r < l:
                r += 1
            while r >= l and l < len(height):
                if r == l:
                    if r < len(height) - 1:
                        r += 1
                area = max(area, ((r - l - 1) * min(height[l], height[r])) - between)
                between += height[r]
                if height[r] >= height[l]:
                    maxarea += area
                    l = r
                    between = 0
                    area = 0
                r += 1
                if r == len(height):
                    l += 1
                    r -= 1
                    between -= height[r]
                    if l < len(height):
                        between -= height[l]
        return maxarea
test = Solution()
print(test.trap([5,4,1,2]))