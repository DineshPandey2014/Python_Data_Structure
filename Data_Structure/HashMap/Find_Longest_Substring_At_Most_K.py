"""
Example 1: You are given a string s and an integer k. Find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most
2 distinct characters is "ece"

"""


def find_longest_substring(s, k):
    count = {} # dict
    left = 0
    result = 0

    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 1
        else:
            count[s[right]] = count[s[right]] + 1


        while len(count) > k:
            # Decrement the count
            count[s[right]] = count[s[right]] - 1
            # Increment the left
            left = left + 1
            # if the count becomes 0 del the key form dict
            del count[s[right]]
        result = max(result, right - left + 1)

    return result

# Import defaultdict
from collections import defaultdict
# Here using defaultdict
def find_longest_substring_ver2(s, k):
    # Dictionary
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] = counts[s[right]] + 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

if __name__ == "__main__":
    s = "eceba"
    k = 2
    result  = find_longest_substring_ver2(s, 2)
    print(result)




