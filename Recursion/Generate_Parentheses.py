def generateParenthesis(n):
    open_bracket_count = 0
    close_bracket_count = 0
    # Here we will take the list to add all the character of the brackets
    # and then will join when we see that the length of the list is equal the total number of character 2 * n
    result = []

    def generate_all_parenthese(curr_str, open_bracket_count, close_bracket_count):
        # base case
        # When the length of curr string equals to 2 * n it means we have one well formed
        # set of brackets add to the list
        if len(curr_str) == 2 * n:
            result.append("".join(curr_str))
            return

        # Keep adding left bracket till the count is less
        if open_bracket_count < n:
            curr_str.append("(")
            generate_all_parenthese(curr_str, open_bracket_count + 1, close_bracket_count)
            # Here we need to pop the element which we added
            # Reason of dong that we need to get back to same state after recursion return
            curr_str.pop()

        if close_bracket_count < open_bracket_count:
            curr_str.append(")")
            generate_all_parenthese(curr_str, open_bracket_count, close_bracket_count + 1)
            curr_str.pop()

    generate_all_parenthese([], open_bracket_count, close_bracket_count)
    return result

if __name__ == "__main__":
    result = generateParenthesis(2)

