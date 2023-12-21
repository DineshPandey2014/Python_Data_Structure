from collections import defaultdict

def intersection(nums):
    # Here we need to return the array that is in all the list.
    # Trick we need to find the number count if it is 3 means it repeated in all three hasmap

    # nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    result = defaultdict(int)

    # Create a dictionay with count in the list
    for outer in nums:
        for i in range(len(outer)):
            result[outer[i]] = result[outer[i]] + 1

    array_length = len(nums)

    ans = []
    #defaultdict(<class 'int'>, {3: 3, 1: 2, 2: 2, 4: 3, 5: 2, 6: 1})
    for key, value in result.items():
        if array_length == value:
            ans.append(key)
    ans.sort()
    return ans

if __name__ == "__main__":

    x = [[3,1,2,4,5],
         [1,2,3,4],
         [3,4,5,6]]

    ans  = intersection(x)
    print(ans)
