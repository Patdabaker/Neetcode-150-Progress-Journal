"""
Problem: Minimum Window Substring
Link: https://neetcode.io/problems/minimum-window-with-characters?list=neetcode150
Category: Sliding Window
Created on: 6/15/2025

Approach:
-
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        res = ""
        sdict = {}
        tdict = {}
        for letter in t:
            tdict[letter] = tdict.get(letter, 0) + 1
            if letter not in s:
                return res
        l = 0
        shortest = len(s)
        sub = [0] * 2
        while s[l] not in tdict:
            l += 1
        for r in range(l, len(s)):
            if s[r] in tdict:
                sdict[s[r]] = sdict.get(s[r], 0) + 1
                while sdict[s[r]] > tdict[s[r]]:
                    if s[l] in tdict:
                        sdict[s[l]] = sdict.get(s[l], 0) - 1
                        l += 1
                    else:
                        l += 1
            if sdict == tdict:
                if r - l <= shortest:
                    shortest = r - l
                    sub[0], sub[1] = l, r
                sdict[s[l]] = sdict.get(s[l], 0) - 1
                l += 1
            while l < len(s) and s[l] not in tdict:
                l += 1
        for i in range(sub[0], sub[1] + 1):
            res += s[i]
        return res

test = Solution()
print(test.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))