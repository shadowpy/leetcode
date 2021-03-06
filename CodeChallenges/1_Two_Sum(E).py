"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""




class Solution:
     """
     i = [0, 1, 2, 5]
     j = [1, 2, 3, 4]
     
     iterates through list and returns index i, j
     """


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums) ):
                if (nums[i] + nums[j]) == target:
                    return i, j














 

