"""
https://leetcode.com/problems/maximum-average-subarray-i/
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and

return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


def findMaxAverage(nums, k):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum = curr_sum + num
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    x = [1,12,-5,-6,50,3]

    k = 4
    result = findMaxAverage(x, k)
    print(result)
