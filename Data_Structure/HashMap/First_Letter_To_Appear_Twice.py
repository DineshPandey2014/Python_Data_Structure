def repeatedCharacter(s: str) -> str:
    # Here we define the set as x = set()
    # x.add()
    seent_set = set()
    for character in s:
        if character in seent_set:
            # Return first character
            return character
        seent_set.add(character)

# Iterate string as index
def iterate_string_as_index(x_str):
    # iterate string as character using index
    for i in range(len(x_str)):
        print(x_str[i])

# Iterate String as character without index
# Iterate string as index
def iterate_string_as_without_index(x_str):
    # iterate string as character using index
    for character in x_str:
        print(character)

def repeatedCharacter(s: str) -> str:
    for i in range(len(s)):
        c = s[i]
        for j in range(i):
            if s[j] == c:
                return c

    return ""

if __name__ == "__main__":
    s = "abccbaacz"
    #result = repeatedCharacter(s)
    result = repeatedCharacter(s)
    print(result)

