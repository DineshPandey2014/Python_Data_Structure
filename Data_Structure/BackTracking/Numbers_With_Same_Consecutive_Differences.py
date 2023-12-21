"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/

Numbers With Same Consecutive Differences

Given two integers n and k, return an array of all the integers of length n
 where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.


"""

def numsSameConsecDiff(n, k):
    result = []

    if n == 1:
        return [i for i in range(10)]

    def dfs(num, n):
        if n == 0:
            result.append(num)
            return

        last_digit = num % 10

        if last_digit + k < 10:
            dfs(num * 10 + last_digit + k, n - 1)

        if k != 0 and last_digit - k >= 0:
            dfs(num * 10 + last_digit - k, n - 1)



    for i in range(1, 10):
        dfs(i, n -1)

    return result

if __name__ == "__main__":
    N = 2
    K = 1
    result = numsSameConsecDiff(N, K)
    print(result)