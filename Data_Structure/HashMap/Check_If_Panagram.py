"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return

true if sentence is a pangram, or false otherwise.

To get a ascii character a
Use => chr(ord('a') + 0)


Python String find() method returns the lowest index or first occurrence of the substring
if it is found in a given string. If it is not found, then it returns -1.

Syntax: str_obj.find(sub, start, end)

Parameters:

sub: Substring that needs to be searched in the given string.
start (optional): Starting position where the substring needs to be checked within the string.
end (optional): End position is the index of the last value for the specified range. It is excluded while checking.
Return:  Returns the lowest index of the substring if it is found in a given string. If it’s not found then it returns -1.
"""

# Time complexity os O(N)
def checkIfPangram_ver_1(sentence: str) -> bool:
    # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
        for i in range(26):
            curr_char = chr(ord('a') + 1)
        # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
            if sentence.find(curr_char) == -1:
                return False

    # If we manage to find all 26 letters, it is a pangram.
        return True

# This is better version iterate sentence. Add all the characters to set.
# If the length of set is 26 characters than it means we have all the 26 characters
def checkIfPangram_ver_2(sentence: str) -> bool:
    seen_set = set(sentence)
    if len(seen_set) == 26:
        return True
    return False

# This is better version iterate sentence. Add all the characters to set.
# If the length of set is 26 characters than it means we have all the 26 characters
def checkIfPangram_ver_3(sentence: str) -> bool:
    seen_set = set(sentence)
    if len(seen_set) == 26:
        return True
    return False

if __name__ == "__main__":
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    result = checkIfPangram_ver_1(sentence)
    print(result)