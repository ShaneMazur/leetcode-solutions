'''
Problem:
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Ex.
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if matrix:
            n = [0, len(matrix[0])]
            m = [0, len(matrix)]
            while True:
                result += [matrix[m[0]][i] for i in range(n[0],n[1])]
                m = [m[0]+1,m[1]]
                if len(result) == len(matrix)*len(matrix[0]):
                    break
                result += [matrix[i][n[1]-1] for i in range(m[0],m[1])]
                n = [n[0],n[1]-1]
                if len(result) == len(matrix)*len(matrix[0]):
                    break
                result += [matrix[m[1]-1][i-1] for i in range(n[1],n[0],-1)]
                m = [m[0],m[1]-1]
                if len(result) == len(matrix)*len(matrix[0]):
                    break
                result += [matrix[i-1][n[0]] for i in range(m[1],m[0],-1)]
                n = [n[0]+1,n[1]]
                if len(result) == len(matrix)*len(matrix[0]):
                    break
        return result