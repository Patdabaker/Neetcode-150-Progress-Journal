"""
Problem: Valid Anagram
Link: https://neetcode.io/problems/is-anagram?list=neetcode150
Category: Arrays & Hashing
Created on: 6/9/2025

Approach:
- Compare lengths of both strings, return False if different
- Create two 0 arrays of length 26 for each character in alphabet, all lowercase
- Compare if both arrays are equal, return True if so
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sarray = [0] * 26
        tarray = [0] * 26
        for i in range(len(s)):
            sarray[ord(s[i]) - ord('a')] += 1
            tarray[ord(t[i]) - ord('a')] += 1
        return sarray == tarray