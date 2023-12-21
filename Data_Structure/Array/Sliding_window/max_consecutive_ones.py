"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's
in the array if you can flip at most k 0's.

Here we need to find the max string of 1's by flipping k at mose '0's
It means our window size will have max 0's of length k
"""


def longestOnes(nums, k):
    left = 0
    # count of 0's in the string
    curr = 0

    # Max string of 1's and 0's. Which have at most k zeros
    result = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            curr = curr + 1

        while curr > k:
            if nums[left] == 0:
                curr = curr - 1
            left = left + 1

        result = max(result, right - left + 1)

    return result

if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    #nums = [1, 1, 0, 0, 1,0]
    k = 2
    result = longestOnes(nums, 2)
    print(result)