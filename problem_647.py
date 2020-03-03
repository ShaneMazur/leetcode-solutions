'''
Problem:
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Note:The input string length won't exceed 1000.

Ex.
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        l,k = len(s),0
        for i in range(l):
            for m,n in [(i,i),(i,i+1)]:
                while 0 <= m and n < l and s[m] == s[n]:
                    k,m,n = k+1,m-1,n+1
        return k