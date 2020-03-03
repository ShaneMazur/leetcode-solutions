'''
Problem:
Given an integer, write a function to determine if it is a power of three.

Ex.
Input: 27
Output: true

Input: 0
Output: false

Input: 9
Output: true

Input: 45
Output: false

'''
from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else abs(log(n,3) - round(log(n,3))) < 10e-11