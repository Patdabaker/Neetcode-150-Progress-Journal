"""
Problem: Longest Substring Without Repeating Characters
Link: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150
Category: Sliding Window
Created on: 6/14/2025

Approach:
- Used sliding window to calculate the largest window in the array
- Added to dictionary for new character, and adjusted l and dictionary for duplicates
- Obtained the largest streak and returned
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        check = {}
        longest = 0
        streak = 0
        for r in range(len(s)):
            while s[r] in check:
                del check[s[l]]
                l += 1
                streak -= 1
            check[s[r]] = check.get(s[r], 0) + 1
            streak += 1
            longest = max(longest, streak)
        return longest
test = Solution()
print(test.lengthOfLongestSubstring("xxxx"))