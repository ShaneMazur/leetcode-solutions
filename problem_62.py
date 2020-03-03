'''
Problem:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to
reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Ex.
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28

'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 1
        for x in range(m+n-2):
            answer *= x+1
        for x in range(m-1):
            answer /= x+1
        for x in range(n-1):
            answer /= x+1
        return round(answer)
