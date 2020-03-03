'''
Problem:
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Ex.
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = [[0 for i in range(n)] for i in range(n)]
        k = 0
        i = 1
        while i <= n**2:
            for j in range(k,n-k):
                spiral[k][j] = i
                i+= 1
            if i > n**2:
                break
            for j in range(k+1,n-k):
                spiral[j][n-k-1] = i
                i+= 1
            if i > n**2:
                break
            for j in range(n-k-1,k,-1):
                spiral[n-k-1][j-1] = i
                i+= 1
            if i > n**2:
                break
            for j in range(n-k-1,k+1,-1):
                spiral[j-1][k] = i
                i+= 1
            if i > n**2:
                break
            k += 1
        return spiral
