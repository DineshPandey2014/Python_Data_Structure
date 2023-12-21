"""
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means,
after reversing it, it is still the same string. For example: "abcdcba", or "racecar".


Space Complexity => Space complexity is fixed which is Order of 1 O(1)
Time Complexity => O(n)
"""
def check_palindrome(s):
    left = 0
    right = len(s) -1

    while(left < right):
        if s[left] == s[right]:
            left = left + 1
            right = right -1
        else:
            return False

    return True

if __name__ == "__main__":
    print(check_palindrome("d"))


