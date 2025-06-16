"""
Problem: Permutation in String
Link: https://neetcode.io/problems/permutation-string?list=neetcode150
Category: Sliding Window
Created on: 6/15/2025

Approach:
- Used sliding window on s2 with the size of the window being the length of s1
- Returned false if s1 was greater than s2
- Counted the number of characters of both strings by the length of s1 and put them into their own 0 array
- If all numbers matched, returned true
- For the rest of s2, slid the window until either both arrays matched or reached the end
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1array = [0] * 26
        s2array = [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1array[ord(s1[i]) - ord('a')] += 1
            s2array[ord(s2[i]) - ord('a')] += 1
        matching = 0
        for i in range(len(s1array)):
            if s1array[i] == s2array[i]:
                matching += 1
        l = 0
        for r in range(len(s1), len(s2)):
            s2array[ord(s2[r]) - ord('a')] += 1
            s2array[ord(s2[l]) - ord('a')] -= 1
            if s1array == s2array:
                return True
            l += 1
        return matching == 26

test = Solution()
print(test.checkInclusion('abc', 'bbbbca'))