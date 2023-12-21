"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/

https://www.geeksforgeeks.org/longest-subarray-sum-elements-atmost-k/

Given an array of positive integers nums and an integer k, find the length of the longest subarray
whose sum is less than or equal to k. This is the problem we have been talking about above.
We will now formally solve it.

Time Complexity O(N)

A sliding window guarantees a maximum of 2N iterations.
window iterations - the right pointer can move n times and the left pointer can move n times.
This means if the logic done for each window is O(1)

sliding window algorithms run in O(N) which is much faster.


You may be thinking: there is a while loop inside of the for loop, isn't the time complexity O(n^2)
The reason it is still O(n) is that the while loop can only iterate n times in total for the entire algorithm
 (left starts at 0, only increases, and never exceeds n). If the while loop were to run n times on
 one iteration of the for loop, that would mean it wouldn't run at all for all the other
  iterations of the for loop. This is what we refer to as amortized analysis - even though
  the worst case for an iteration inside the for loop is O(n), it averages out to O(1)
  when you consider the entire runtime of the algorithm.


"""
#
def longest_subarray_sum_less_than_equal_k(nums, k):
    left_index = 0
    max_sum = 0
    # Max window after each iteeration
    max_subarray_window_length = 0

    for right_index, elem in enumerate(nums):
        max_sum = max_sum + elem
        while max_sum > k:
            max_sum = max_sum - nums[left_index]
            left_index = left_index + 1
        max_subarray_window_length = max(max_subarray_window_length,  right_index - left_index + 1)
    return max_subarray_window_length

if __name__ == "__main__":
    nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    k = 8.
    result = longest_subarray_sum_less_than_equal_k(nums, k)
    print(result)


