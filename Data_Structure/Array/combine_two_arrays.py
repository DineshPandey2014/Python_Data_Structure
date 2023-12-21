# Given both array are sorted
def combine_two_arrays(arr1:list[int],arr2:list[int]):
    result = []
    x = 0
    y = 0
    while(x < len(arr1) and y < len(arr2)):
        if arr1[x] <= arr2[y]:
            result.append(arr1[x])
            x = x +1
        else:
            result.append(arr2[y])
            y = y + 1

    while x < len(arr1):
        result.append(arr1[x])
        x = x +1

    while y < len(arr2):
        result.append(arr2[y])
        y = y +1

    return result

if __name__ == "__main__":
    result = combine_two_arrays([], [])
    print(result)






