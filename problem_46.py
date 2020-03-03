'''
Problem:
Given a collection of distinct integers, return all possible permutations.

Ex.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
from itertools import product

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]
        for num in nums:
            permutations = [x+[y] for x,y in product(permutations,nums) if y not in x]
        return permutations
