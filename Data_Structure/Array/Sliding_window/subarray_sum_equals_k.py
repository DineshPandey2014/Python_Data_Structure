"""
Example 4: Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.

Find the largest window. Window size is fixed.
Algo => Here window size is fixed.

1) Create the window. Left pointer will be in 0 index
   right pointer will be at index k

2)

"""

def find_best_subarray(nums, k): # Create a window of size k
    # holds current sum
    curr = 0

    # holds max sum
    result = 0
    for i in range(k):
        curr = curr + nums[i]
    #Holds the sum of first window size k
    result = curr
    left = k-1
    for right in range(k, len(nums)):
        curr = curr + nums[right]
        if curr > k:
            curr = curr - nums[left]
        result = max(result, curr)
    return result

if __name__ == "__main__":
    result = find_best_subarray([3,-1,4,12,-8,5,6], 4)
    print(result)














