"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,

typically using all the original letters exactly once.

https://leetcode.com/problems/group-anagrams/description/
"""

from collections import defaultdict

"""
Time complexity 
Each string K character
Sort each string time complexity  k log k
Total N String => Time Complexity => N(K log K)
"""
def groupAnagrams(strs):
    anagram_dict = defaultdict(list)

    for s in strs:
        s_list = list(s)
        s_list.sort()
        after_sort = "".join(s_list)
        anagram_dict[after_sort].append(s)
    return anagram_dict.values()
