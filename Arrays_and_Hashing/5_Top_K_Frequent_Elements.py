"""
Problem: Top K Frequent Elements
Link: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
Category: Arrays & Hashing
Created on: 6/9/2025

Approach:
- Use dictionary to store frequency values
- Obtains top k values using max function and appending to list
"""
class Solution:
    def topKFrequent(self, nums, k: int):
        numsdict = {}
        res = []
        for num in nums:
            numsdict[num] = numsdict.get(num, 0) + 1
        while k > 0:
            largest = max(numsdict, key=numsdict.get)
            res.append(largest)
            del numsdict[largest]
            k -= 1
        return res