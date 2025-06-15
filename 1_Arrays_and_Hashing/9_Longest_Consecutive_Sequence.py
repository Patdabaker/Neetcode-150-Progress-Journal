"""
Problem: Longest Consecutive Sequence
Link: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
Category: Arrays & Hashing
Created on: 6/11/2025

Approach:
- Sorted the list nums and made it a set
- Checked whether the previous number in the list was consecutive and added to a counter
- Obtained the max of either the previous longest or current longest
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        count = 1
        longest = 1
        if not nums:
            return 0
        if len(nums) == 0:
            return count
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                longest = max(count, longest)
            else:
                count = 1
        return longest

