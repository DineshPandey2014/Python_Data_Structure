def is_sorted_in_ascending_order(a):
    length = len(a)
    b = []
    for i in range(length):
        if i % 2:
            b.append(a[length - (i // 2) - 1])    # Updated.
        else:
            b.append(a[i // 2])                   # Updated.

    print(b)
    # Check if the new array b is sorted in strictly ascending order
    for i in range(1, len(b)):
        if abs(b[i]) < abs(b[i - 1]):
            return False

    return True

if __name__ == "__main__":
    # a = [-99, -29, -7, 17, 28, 71, 98, 86, 42, 22, 0, -29, -86]
    # result1 = is_sorted_in_ascending_order(a)
    # print(result1)

    a1 = [1, 3, 5, 6, 4, 2]
    result2 = is_sorted_in_ascending_order(a1)
    print(result2)