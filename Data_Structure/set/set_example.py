"""
Example 3: Given an integer array nums, find all the numbers x in nums that satisfy the
following: x + 1 is not in nums, and x - 1 is not in nums.

Algo :
Will use set
Add all the elements of list to set
Iterate nums and check if x +1 and x - 1 not in nums
Add all the elements to list as result
return result

Time complexity is O(N)
Sapce compexity is O(1)

"""
def find_numbers(nums):
    # Add all the elements in the set without iterate
    set_all_elements = set(nums)
    result = []
    for i in range(len(nums)):
        if nums[i] + 1 not in set_all_elements and nums[i] - 1 not in set_all_elements:
            result.append(nums[i])
    return result

