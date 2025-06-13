"""
Problem: 3Sum
Link: https://neetcode.io/problems/three-integer-sum?list=neetcode150
Category: Two Pointers
Created on: 6/12/2025

Approach:
- Used two pointer technique
- Sorted list of numbers, then checked for triplets for each number using two pointers
- Appended to list if triplet was equal to 0 and not in the list already
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(1, len(nums) - 1):
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if s > 0:
                    r -= 1
                if s < 0:
                    l += 1
                if s == 0:
                    if l == i or l == r or i ==r:
                        r -= 1
                        l += 1
                    else:
                        triple = [nums[l], nums[i], nums[r]]
                        triple.sort()
                        if triple not in ans:
                            ans.append(triple)
                        r -= 1
                        l += 1
        return ans

test = Solution()
print(test.threeSum([]))