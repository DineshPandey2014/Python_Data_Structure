"""
https://leetcode.com/problems/permutations/

https://www.youtube.com/watch?v=H232aocj7bQ

Given an array nums of distinct integers, return all
the possible permutations. You can return the answer in any order.

"""
def find_permutation_backtrack(nums, tmp, result):
    # Base Case
    # If we match a length it's a permutaiton
    if len(tmp) == len(nums):
        result.append(tmp.copy())
        return

    for num in nums:
        if num not in tmp:
            tmp.append(num)
            find_permutation_backtrack(nums, tmp, result)
            tmp.pop()


if __name__ == "__main__":
    nums = [1,2]
    curr = []
    final_result = []
    result = find_permutation_backtrack(nums,curr, final_result)
    print(final_result)