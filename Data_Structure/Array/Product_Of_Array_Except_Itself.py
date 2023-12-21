"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


def productExceptSelf( nums):
    prefix = []
    prv_prod_prefix = 1

    for index in range(0, len(nums)):
        num = nums[index]
        prefix.append(prv_prod_prefix)
        prv_prod_prefix = prv_prod_prefix * num

    suffix = []
    prv_prod_suffix = 1

    for index in range(len(nums)-1, -1, -1):
        num = nums[index]
        suffix.insert(0, prv_prod_suffix * prefix[index])
        prv_prod_suffix = prv_prod_suffix * num
    return suffix

    # result = []
    # for index in range(0, len(prefix)):
    #     prod = prefix[index] * suffix[index]
    #     result.append(prod)
    # return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    result = productExceptSelf(nums)
    print(result)
