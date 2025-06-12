"""
Problem: Valid Palindrome
Link: https://neetcode.io/problems/is-palindrome?list=neetcode150
Category: Two Pointers
Created on: 6/11/2025

Approach:
-
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
            if left > right:
                return False
        return True
test = Solution()
print(test.isPalindrome(",..,..."))