"""

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

"""

# Input: nums[1, 2, 3, 4]
# Output: nums[1, 3, 6, 10]

class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# Basically, we want [1, 1+2, 1+2+3, 1+2+3+4]

# To do this, we loop through the values
# (1 in range represents the first value and makes it so it is not 0)
# (len(nums) represents the length of the array)

# nums[i-1] takes the value of the last element in the array
# so when you loop through, for the first round, it will only be i
# the second round, it will be i and i-1 which is 2 so our function gives us 1 + 2
# the third round, it will be i which is 1 and 2, and i-1 which is 3 so our function gives us 1 + 2 + 3

