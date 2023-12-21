def isValid(self, s: str) -> bool:
    # Time Complexity O(N) . As we are traversing each character once
    # Sppce complexity worst case O(N)
    # use list as stack
    # Keep pushing the character to list.
    # If any closing char comes in the String means ")" , "}", "]"
    # then pop from the list it should match with the correspind character
    # mean ) => (
    #      } => {
    #      ] => ]
    result = []

    if s == None:
        return False

    for i in range(len(s)):
        elem = s[i]
        if elem == ")" and len(result) > 0 and result[-1] == "(":
            # pop the element from the list
            result.pop()
        elif elem == "}" and len(result) > 0 and result[-1] == "{":
            # pop the element from the list
            result.pop()
        elif elem == "]" and len(result) > 0 and result[-1] == "[":
            # pop the element from the list
            result.pop()
        else:
            result.append(elem)
    return len(result) == 0