"""
Problem: Encode and Decode Strings
Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
Category: Arrays and Hashing
Created on: 6/9/2025

Approach:
- Append string starting with length of string, followed by string and character '$'
- Decodes using the integer and '$' to determine individual strings
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s.append(str(len(word)))
            for letter in word:
                s.append(letter)
            s.append('$')
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        full = ''
        for i in range(len(s)):
            if s[i].isdigit() and not full:
                continue
            elif s[i] == '$':
                strs.append(full)
                full = ''
            else:
                full.append(s[i])
        return strs