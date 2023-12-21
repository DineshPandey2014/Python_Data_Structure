"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/

https://leetcode.com/problems/is-subsequence/

Given two string s and t, return true id s is a subsequence of t or false otherwise.
A subsequence of a String is a sequence of the characters from the original string. While maintaining
the relative order of the remaining characters.

For ace is subsequence of abcde

while aec is not a subsequence of "abcde"
"""

def subsequence(input_one:str, input_two:str)-> bool:
    i = 0
    j = 0
    while(i < len(input_one) and j < len(input_two)):
        if input_one[i] == input_one[j]:
            i = i + 1
        j = j +1

    return i == len(input_one)

if __name__ == "__main__":
    print(subsequence("dnep", "dinesh"))





