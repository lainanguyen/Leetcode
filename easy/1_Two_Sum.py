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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, (len(nums))):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]