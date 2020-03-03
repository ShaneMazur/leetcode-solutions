'''
Problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Ex.
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted_nums = {}

        # Iterating through a list of numbers
        for i in range(len(nums)):

            # If number in wanted_nums it means we've got the sum!
            if nums[i] in wanted_nums:
                return [wanted_nums[nums[i]], i]

            # If not, we store the difference (so the number we seek) along with an index
            else:
                wanted_nums[target - nums[i]] = i
