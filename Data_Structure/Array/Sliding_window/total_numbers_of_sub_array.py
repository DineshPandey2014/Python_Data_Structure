"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

"""


def subarraySum(self, nums, k):
    left = 0
    curr_sum = 0
    result = 0

    for right in range(len(nums)):
        curr_sum = curr_sum + nums[right]

        if curr_sum == k:
            result = result + right - left + 1

        if curr_sum > k:
            curr_sum = curr_sum - nums[left]
            left = left + 1

    return result