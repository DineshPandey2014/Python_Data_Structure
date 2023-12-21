def binary_search_recursive(num_list, elem, left, right):
    mid = (right +left) //2

    if left > right:
        return

    if num_list[mid] == elem:
        return mid, elem
    elif num_list[mid] < elem:
        # Move right
        return binary_search_recursive(num_list, elem, mid + 1,  right)
    else:
        # Move left
        return binary_search_recursive(num_list, elem, left, mid-1)


if __name__ == "__main__":
    list = [12,13,14,17,18,19]
    left = 0
    elem = 14
    right = len(list) -1
    result = binary_search_recursive(list, elem, left, right)
    print(result[0])
    print(result[1])