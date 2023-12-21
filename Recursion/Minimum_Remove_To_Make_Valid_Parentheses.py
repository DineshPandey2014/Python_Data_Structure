def minRemoveToMakeValid(s: str):
    """
    Take the stack.
    push the opening brackets to stack. Here we push the index of the bracket
    If there is a closing brackets pop the matching element from the stack
    In the last we have left only non matching braces left.
    """

    stack = []

    for i in range(len(s)):
        element = s[i]

        if element == "(":  # open bracket push the element to Stack. Here we will push the index
            stack.append(i)
        elif element == ")":
            if len(stack) > 0 and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)

    result = []
    for i in range(len(s)):
        if i not in stack:
            result.append(s[i])

    return "".join(result)

if __name__ == "__main__":
    x = "lee(t(c)o)de)"
    result = minRemoveToMakeValid(x)
    print(result)
