'''
Problem:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Ex.
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zeros = [i for i in range(len(nums)-1) if nums[i] == 0]
        s = 0
        for i in zeros:
            jumped = False
            for j in range(s,i):
                if j+nums[j] > i:
                    jumped = True
                    break
            if not jumped:
                return False
        return True
