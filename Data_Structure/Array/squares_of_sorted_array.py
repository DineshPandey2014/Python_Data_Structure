"""
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

"""
def sortedSquares_ver_1(nums):
    """
    Approach: Take two pointers left and right(End of the length of the string)

    1: Use while loop left <= right
    2: swap the item
    3: square the item
    It will be doing in place swap and squaring the array

    Time complexity is => O(n log (n))
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        temp = nums[left]
        nums[left] = nums[right] * nums[right]
        nums[right] = temp * temp
        left = left + 1
        right = right - 1

    nums.sort(reverse=True)

# """
# Time complexity O(nlog(n)
# """
# def sortedsquares_ver_2(nums):
#     result = sorted(x * x for x in nums)
#     return result

def sortedsquare_ver_3(nums):
    left = 0
    right = len(nums) -1

def sortedSquares(nums):
    """
    Approach: Take two pointers left and right(End of the length of the string)

    1: Use while loop left <= right
    2: swap the item
    3: square the item
    It will be doing in place swap and squaring the array

    return sorted(x * x for x in nums)
    """
    # This algo is O(n) time complexity
    # Space O(n)
    left = 0
    right = len(nums) - 1
    # Array size of n
    result = len(nums) * [0]
    i = len(nums) - 1
    while left <= right:
        x = nums[left] * nums[left]
        y = nums[right] * nums[right]

        if (x < y):
            result[i] = y
            right = right - 1
            i = i - 1
        elif (x > y):
            result[i] = x
            i = i - 1
            left = left + 1
        else:
            result[i] = x
            left = left + 1
            i = i - 1

    return result


if __name__ =="__main__":
    x = [2,2,2]
    result = sortedSquares(x)
    print(result)

