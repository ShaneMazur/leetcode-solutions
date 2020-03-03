'''
Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

Ex.
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        NUMBERS = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        results = []
        for digit in digits:
            if len(results) == 0:
                results = NUMBERS[digit]
            else:
                results = [x + y for x, y in product(results, NUMBERS[digit])]
        return results