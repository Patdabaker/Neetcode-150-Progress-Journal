"""
Problem: Valid Palindrome
Link: https://neetcode.io/problems/is-palindrome?list=neetcode150
Category: Two Pointers
Created on: 6/11/2025

Approach:
- Used the two pointer approach to tackle this problem
- Used a pointer on opposite sides and moved until they met up
- Ignored non-alphanumeric characters
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
                else:
                    left += 1
                    right -= 1

        return True
test = Solution()
print(test.isPalindrome("was it a car or a cat i saw"))