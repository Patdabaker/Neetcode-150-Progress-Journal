"""
Problem: Products of Array Except Self
Link: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
Category: Arrays & Hashing
Created on: 6/10/2025

Approach:
- Used the prefix and suffix method to solve without using divisor operator
- Found pre and suf for forward and backwards list respectively
- Reversed suf and multiplied each index by pre to get the result
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1] * len(nums)
        suf = [1] * len(nums)
        res = [1] * len(nums)
        previous = 1
        for i in range(len(nums) - 1):
            pre[i + 1] = previous * nums[i]
            previous = pre[i + 1]
        previous = 1
        for i in range(len(nums) - 1):
            suf[i + 1] = previous * nums[-i - 1]
            previous = suf[i + 1]
        suf.reverse()
        for i in range(len(nums)):
            res[i] = pre[i] * suf[i]
        return res