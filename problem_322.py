'''
Problem:
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Ex.
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
'''
from itertools import product

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = 0
        lox = [0]
        tot_lox = set()
        while lox and amount not in lox:
            n += 1
            lox = set([sum(x) for x in product(lox,coins) if sum(x) <= amount]) - tot_lox
            tot_lox = tot_lox | lox
        return n if lox else -1