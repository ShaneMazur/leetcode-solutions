'''
Problem:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Ex.
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
from itertools import product
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        permutations = [tuple()]
        for num in nums:
            permutations = set([x+(y,) for x,y in product(permutations,nums) if Counter(x)[y] < count[y]])
        return permutations