"""
Minimum Value to Get Positive Step by Step Sum
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1
"""

"""

First, let's iterate over the array using 0 as the initial value and we will have a list 
that consists of all step-by-step sums, where the minimum total is -4. Therefore, we shall 
choose the startValue that changes this minimum total from -4 to exactly 1, that is, -4 + startValue = 1. Hence, 
startValue = 5 is the minimum valid startValue for this array.

Algorithm

Traverse the array nums and calculate every step-by-step total, use total to 
record the current step-by-step total, and minVal to record the minimum step-by-step total.
Return -minVal + 1, that is the minimum valid startValue.

"""


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        sum_over = 0

        for i in range(len(nums)):
            sum_over = sum_over + nums[i]

            min_val = min(min_val, sum_over)

        return -min_val + 1
