"""
Problem: Group_Anagrams
Link: https://neetcode.io/problems/anagram-groups?list=neetcode150
Category: Arrays & Hashing
Created on: 6/9/2025

Approach:
- Use dictionary to store and append values of strings that are anagrams
- Use 0 array of length 26 to check if strings were anagrams
- Stored a tuple of the arrays with a value of the string to dictionary
- Return a list of the values in the dictionary
"""
class Solution:
    def groupAnagrams(self, strs):
        grouped = {'empty': []}
        for i in range(len(strs)):
            if not strs[i]:
                grouped['empty'].append(strs[i])
            else:
                charset = [0] * 26
                for j in range(len(strs[i])):
                    charset[ord(strs[i][j]) - ord('a')] += 1
                if tuple(charset) not in grouped:
                    grouped[tuple(charset)] = [strs[i]]
                else:
                    grouped[tuple(charset)].append(strs[i])
        return list(value for value in grouped.values() if value)

