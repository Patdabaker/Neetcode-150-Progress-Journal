"""
Problem: Two Sum
Link: https://neetcode.io/problems/two-integer-sum?list=neetcode150
Category: Arrays & Hashing
Created on: 6/9/2025

Approach:
- Use a dictionary to value with its index
- Calculates compliment number with current value and checks if in dictionary
- Returns the pair that adds up to target
"""
class Solution:
    def twoSum(self, nums, target: int):
        numsdict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numsdict:
                return [numsdict[compliment], i]
            numsdict[nums[i]] = i