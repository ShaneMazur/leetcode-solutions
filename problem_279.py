'''
Problem:
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Ex.
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
    used = {}
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        elif n not in Solution.used:
            l = int(pow(n,0.5))
            Solution.used[n] = 1+min([self.numSquares(n-pow(k,2)) for k in range(l,max(l-16,0),-1)])
        return Solution.used[n]