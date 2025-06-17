"""
Problem: Sliding Window Maximum
Link: https://neetcode.io/problems/sliding-window-maximum?list=neetcode150
Category: Sliding Window
Created on: 6/16/2025

Approach:
- Used sliding window of fixed variable to find the max of the current window along with index
- If current max left window, found new max with index
- If newest number in window was greater, then that became new max
"""
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        maxin = [float("-infinity"), 0] # [value, index]
        for i in range(k):
            if nums[i] >= maxin[0]:
                maxin[0], maxin[1] = nums[i], i
        res.append(maxin[0])
        l = 0
        for r in range(k, len(nums)):
            l += 1
            if l > maxin[1]:
                maxin = [float("-infinity"), 0]
                for i in range(l, l + k):
                    if nums[i] >= maxin[0]:
                        maxin[0], maxin[1] = nums[i], i
            if nums[r] >= maxin[0]:
                maxin[0], maxin[1] = nums[r], r
            res.append(maxin[0])
        return res

test = Solution()
print(test.maxSlidingWindow([1,3,1,2,0,5], 3))
