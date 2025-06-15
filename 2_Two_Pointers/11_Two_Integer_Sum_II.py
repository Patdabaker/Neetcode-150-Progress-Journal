"""
Problem: Two Integer Sum II
Link: https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150
Category: Two Pointers
Created on: 6/12/2025

Approach:
- Used two pointer approach with one pointer on each end
- Decreased right if the numbers pointed at were greater than target
- Increased left if the numbers pointed at were less than target
- Once reached, returned pointers + 1 for a 1 index array
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            if s < target:
                l += 1
            if s == target:
                return [l + 1, r + 1]
        return [l + 1, r + 1]

test = Solution()
print(test.twoSum([1,2,3,5,7,8,9], 7))