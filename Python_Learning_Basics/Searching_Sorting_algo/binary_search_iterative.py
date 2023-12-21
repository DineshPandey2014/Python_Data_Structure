"""
Iterative approach :-

For binary search list should be in sorted order.

"""

def iter_binary_search(numbers, num):
    # Left index
    left = 0

    # Right index
    right = len(numbers)-1

    # <= to ensure the loop runs even when the search space reduces to a single element.
    while left <= right:
        # For integer division we need to divide by two lines
        # a/b => gives float number not integer number  3/2 =>1.5
        mid = (left + right) // 2
        if numbers[mid] == num:
            return mid
        # search to left
        if numbers[mid] < num:
            left = mid +1
        else:
            right = mid -1
    # Not found
    return None


if __name__ == "__main__":
    # List in sorted order
    list_num = [12,13,14,17,18]
    number_to_be_search = 13
    result = iter_binary_search(list_num, number_to_be_search)
    print(result)


