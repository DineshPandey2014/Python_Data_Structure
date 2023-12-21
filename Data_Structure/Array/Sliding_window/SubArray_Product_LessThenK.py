"""
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


"""

def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k <= 1:
        return 0

    left = 0
    # Product of all the items in the sub array
    curr_product = 1

    # result => No of sub array which  product less than k
    result = 0

    for right in range(len(nums)):
        curr_product = curr_product * nums[right]

        while curr_product >= k:
            curr_product = curr_product // nums[left]
            left = left + 1

        result = result + right - left + 1
    return result

if __name__ == "__main__":
    result = numSubarrayProductLessThanK([10,5,2,6], 100)
    print(result)
