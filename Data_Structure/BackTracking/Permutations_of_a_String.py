"""
https://www.youtube.com/watch?v=ZeZU85fZzE0&list=PLNxqWc8Uj2LTaaxs-8vzK0Ft47rMggFnN&index=4

"abc" => Total 6 permutaion will be there

1) ["abc" , "acb", "bac", "bac", "cab", cba"]

"""
def  find_all_permutaion_of_String(input_str, curr_str, result):
    if len(curr_str) == len(input_str):
        result.append("".join(curr_str[:])) # copy curr_str

    for char in input_str:
        if char not in curr_str:
            curr_str.append(char)
            find_all_permutaion_of_String(input_str, curr_str, result)
            curr_str.pop()

if __name__ =="__main__":
    input = "abc"
    input_str = list(input)
    curr_str = []
    result = []
    find_all_permutaion_of_String(input_str, curr_str, result)
    print(result)







