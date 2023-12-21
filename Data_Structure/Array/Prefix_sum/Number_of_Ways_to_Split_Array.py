"""
https://leetcode.com/problems/number-of-ways-to-split-array/
"""

def waysToSplitArray(nums):
    # Add the first element to prefix sum
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    # Here we need at least one element after split on both side
    # So we need to go one element less
    # [10,4,-8,7]
    # Left => [10,4,-8]
    #[7]
    for i in range(len(nums-1)):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans = ans + 1
    return ans

if __name__ == "__main__":
    nums = [10,4,-8,7]
    result = waysToSplitArray(nums)
    print(result)
