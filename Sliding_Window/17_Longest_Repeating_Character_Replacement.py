"""
Problem: Longest Repeating Character Replacement
Link: https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150
Category: Sliding Window
Created on: 6/14/2025

Approach:
-
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        replacement = 0
        for r in range(len(s)):
            current = s[l]
            if s[r] != current:
                replacement += 1
            if replacement <= k:
                longest = max(longest, r - l + 1)
            else:
                while s[l] == current:
                    l += 1
                replacement -= 2
        return longest
test = Solution()
print(test.characterReplacement("ABBACCA", 1))