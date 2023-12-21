from collections import defaultdict
def subarraySum(nums, k):
    # count subarray sum equals to k
    """
    Sliding window

    1: Iterte the list
    2: keep you left pointer at 0. Increment right index check the sum if equals to K
    3: subarray is contiginous
    4: count => right-left+1 => length of the array
    """
    dict = defaultdict(int)
    prefix_sum = 0
    count = 0
    dict[0] = 1
    for i in range(len(nums)):
        prefix_sum = prefix_sum + nums[i]
        # diff is a key for map
        diff =  prefix_sum - k

        if diff in dict:
            count = count + dict[diff]

        dict[prefix_sum] = dict[nums[i]] + 1
    return count


if __name__ == "__main__":
    nums = [1,2,1,2,1]
    k =  3
    result = subarraySum(nums, k)
    print(result)
