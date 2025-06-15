"""
Problem: Contains Duplicate
Link: https://neetcode.io/problems/duplicate-integer?list=neetcode150
Category: Arrays & Hashing
Created on: 6/9/2025

Approach:
- Use a dictionary to store frequency values
- For each value, check if greater than 1 to show duplicates and return True, else False
"""
class Solution:
    def hasDuplicate(self, nums):
        numsdict = {}
        for num in nums:
            numsdict[num] = numsdict.get(num, 0) + 1
        return any(value > 1 for value in numsdict.values())