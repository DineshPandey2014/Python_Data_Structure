import math


def thirdMax(nums) -> int:
    """
    Time complexity will be O(N)
    Take three pointer:-
    First_Max = -inf
    Second_Max = -inf
    Third_Max = -inf
    """

    # define three numbers

    first_max = -math.inf
    second_max = -math.inf
    third_max = -math.inf

    for num in nums:
        # The number is already used it we need ot skip.
        # As we need to consider uniqe three largest number
        if first_max == num or second_max == num or third_max == num:
            continue

        # If  current number is greater than fist maximum
        # It means this is the greatest number
        # First max becomes second highest
        # Second max become thirs highest number
        if first_max <= num:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif second_max <= num:
            third_max = second_max
            second_max = num
        elif third_max <= num:
            third_max = num

        # If third max was never updated. It means we don't have 3 distinct numbers
    if third_max == -math.inf:
        return first_max

    return third_max

if __name__ == "__main__":
    result_third_highest = thirdMax([3,2,1])
    print(result_third_highest)