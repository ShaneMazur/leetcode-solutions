'''
Problem:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Ex.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s:
            posn = [(i,i+1) for i in range(len(s))]+[(i,i+2) for i in range(len(s)) if i+1 < len(s) and s[i] == s[i+1]]
            while True:
                new = list()
                for sub in posn:
                    if not (sub[0] == 0 or sub[1] == len(s)) and s[sub[0]-1] == s[sub[1]]:
                        new.append((sub[0]-1, sub[1]+1))
                if new:
                    posn = new
                else:
                    return s[posn[-1][0]:posn[-1][1]]
        return s
