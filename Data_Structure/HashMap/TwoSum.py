"""
The time complexity is  O(n) as the hash map operations are
O(1). This solution also uses
O(n) space as the number of keys the hash map will store scales linearly with the input size.

"""
def twoSum(nums, target):
    result = []
    hash_map = {}
    # key => target - key
    # value => index

    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            result.append(i)
            result.append(hash_map[target - nums[i]])
            return result
        else:
            hash_map[target - nums[i]] = nums[i]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    result = twoSum(nums, 9)
    print(result)
