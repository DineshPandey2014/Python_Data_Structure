"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/

Example 2: You are given a binary string s (a string containing only "0" and "1").
You may choose up to one "0" and flip it to a "1". What is the length of the longest
substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2,
the string becomes 1111100111

https://www.geeksforgeeks.org/longest-subsegment-1s-formed-changing-k-0s/

Given a binary array a[] and a number k, we need to find length of the longest subsegment
of ‘1’s possible by changing at most k ‘0’s.

Input : a[] = {1, 0, 0, 1, 1, 0, 1},
          k = 1.
Output : 4
Explanation : Here, we should only change 1
zero(0). Maximum possible length we can get
is by changing the 3rd zero in the array,
we get a[] = {1, 0, 0, 1, 1, 1, 1}

Input : a[] = {1, 0, 0, 1, 0, 1, 0, 1, 0, 1},
         k = 2.
Output : 5
Output: Here, we can change only 2 zeros.
Maximum possible length we can get is by
changing the 3rd and 4th (or) 4th and 5th
zeros.
"""
"""
Allow only one 0. For max substring
"""
def find_length_substring(input_str: str, k) -> int:
    left = 0
    curr = 0
    ans = 0

    for index in range(len(input_str)):
        # Not here we are passing input_str as String "1101100111"
        # Use string comparision
        # if input_str[index] == "0":

        # If we have input as string array [1, 1, 0, 1, 1, 0, 0, 1,1 ,1
        # Use number comparision
        # if input_str[index] == 0:
        if type(input_str) is str and input_str[index] == "0":
            curr = curr + 1
        # elif type(input_str[index]) is int and input_str[index] == 0:
        #     curr = curr + 1
        while curr > k:
            if input_str[left] == "0":
                curr = curr - 1
            left = left + 1
        ans = max(ans, index - left + 1)

    return ans

if __name__ == "__main__":
    nums = "11011"
    k = 2
    print (find_length_substring(nums, k))