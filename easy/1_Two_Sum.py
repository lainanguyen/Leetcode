"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

nums = [1, 2, 3, 5, 1]
target = 4

return [0, 2]
        i  j


"""

class Solution:
    def twoSum(self, nums, target):
        dictionary = dict()
        for i, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], i]
            else:
                dictionary[target-num] = i