"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

def letterCombinations(digits):
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    # Map all the digits to their corresponding letters
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backtrack(index, path):
        # If the path is the same length as digits, we have a complete combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return  # Backtrack

        # Get the letters that the current digit maps to, and loop through them
        possible_letters = letters[digits[index]]
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the letter before moving onto the next
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations


if __name__ == "__main__":
    # Initiate backtracking with an empty path and starting index of 0
    digits = "23"
    result = letterCombinations(digits)
    print(result)
