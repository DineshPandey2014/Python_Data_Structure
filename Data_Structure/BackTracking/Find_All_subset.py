"""
Difference between subset and Permutation
is that
Permutatoin : [1,2]
=> All permutation here we have position matters. It cannot be empty
=>[1,2] , [2,1] => Total 2 permutaiton here [2,1] and [1,2] are different.
=> For permutaion we need all the elements

Set: We can have empty set. set of [1,2] => [], [1] [2], [1,2]
Here we can't ake [2,1] as [1,2] both are same
For set we can have any number of elements. zero element or one element and less
"""
def find_all_subsets(nums, i, result, curr):
    # for base condition we need to check we need to check if i > len(nums) return
    if (i > len(nums)):
        return
    # Add element of curr as copy it. Here in the starting it add empty set
    result.append(curr[:])

    for j in range(i, len(nums)):
        curr.append(nums[j])
        find_all_subsets(nums, j + 1, result, curr)
        curr.pop()

if __name__ == "__main__":
    result = []
    i = 0
    curr = []
    nums = [1,2, 3]
    find_all_subsets(nums, i, result, curr)
    print(result)