"""
Check Third Commit
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
"""


def generateParenthesis(n):
    def generate_all_parenthesis(open_bracket, close_bracket, curr_bracket, result):
        if len(curr_bracket) == 2 * n:
            result.append("".join(curr_bracket))
            return

        if open_bracket < n:
            curr_bracket.append("(")
            generate_all_parenthesis(open_bracket + 1, close_bracket, curr_bracket, result)
            curr_bracket.pop()

        if close_bracket < open_bracket:
            curr_bracket.append(")")
            generate_all_parenthesis(open_bracket, close_bracket + 1, curr_bracket, result)
            curr_bracket.pop()

    curr_bracket = []
    result = []
    open_bracket = 0
    close_bracket = 0
    generate_all_parenthesis(open_bracket, close_bracket, curr_bracket, result)
    return result

if __name__ == "__main__":
    result = generateParenthesis(2)
    print(result)


