"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""
            # 0  1  2  3  4  5
# Input: nums[1, 7, 3, 6, 5, 6]
# Output: Pivot Index is 3
# Because [i=3] = 6, and 1+7+3 = 5+6

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_edge = 0   # It is 0 because it is the initial index, starting point in the array
        for i in range(len(nums)):
            right_edge = total_sum - nums[i] - left_edge    # Total - Middle number - Left Sum
            if left_edge == right_edge:
                return i
            left_edge += nums[i]    #
        return -1

# In the case of nums[1, 7, 3, 6, 5, 6]
# For the first round of the loop, it will return 0 == 28 - 1 - 0 which is False, so it adds 1 to left_edge: 0 + 1
# For the second round, it will return 1 == 28 - 7 - 1 which is False, so it adds 1 again: 1 + 1, so it is now index [2]
# For the third round, it will return 7 == 28 - 7 - 8 which is False, so it adds 1: index [3]
# For the fourth round, it will return 6 == 28 - 6 - 11 which is True, so it returns i which is index [6]
