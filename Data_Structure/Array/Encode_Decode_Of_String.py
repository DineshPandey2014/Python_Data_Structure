
def encode(strs):
    """Encodes a list of strings to a single string.
    """
    # convert int to str
    encode = ""
    for s in strs:
        encode = encode + str(len(s)) + "#" + s
    return encode

def decode(s):
    """Decodes a single string to a list of strings.
    """
    i = 0
    result = []

    """
        1: We need to traverse character by character once we found "#"
        2: Need to slice the string by using operator x[i:j]. It gives the length of the string.
        3: Add string to the result
        res.append(x[j+1 : length_of_string]) # This will return back of the string
        4: Now reset the pointer of i
           i = j+1+length
        5: It moves i to the start of the string
    """

    while i < len(s):
        j = i
        while s[j] != "#":
            j = j + 1
        length_str = int(s[i:j])
        result.append(s[j + 1: j + 1 + length_str])
        i = j + 1 + length_str
    return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))