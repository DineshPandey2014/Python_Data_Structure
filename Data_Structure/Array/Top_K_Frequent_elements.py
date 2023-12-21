from collections import defaultdict
"""
using Bucket sort elements
"""


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    num_dict = defaultdict(int)
    for num in nums:
        num_dict[num] = num_dict[num] + 1  # count frequency
    # Maximum length will be nums + 1 => When each element count one
    # Here we need to increase length by 1. Because 0 can not be count
    # Frequency count start from 1
    freq = [[] for i in range(len(nums) + 1)]

    # Mapped the frequency with index of list. Add key as the number
    for key, value in num_dict.items():
        freq[value].append(key)

    result = []
    # We need to find the top k number start the list in the reverse order
    for feq_list_num in freq[::-1]:
        # Here might be the case to handle the list size > 0
        if len(feq_list_num) > 0:
            # Here we are adding the list items to anpother list it shoud be extend
            result.extend(feq_list_num)
            if len(result) == k:
                return result



    # for i in range(len(freq) -1, 0, -1):
    #     for n in freq[i]:
    #         result.append(n)
    #         if len(result) == k:
    #             return result


if __name__ == "__main__":
    # nums = [1,1,1,2,2,3]
    # k = 2 # top 2 elements
    # result = topKFrequent(nums, k)
    # # Result will be like [0, [2], [1,2]]
    # print(result)

    nums = [1,2]
    k = 2 # top 2 elements
    result = topKFrequent(nums, k)
    print(result)




def topKFrequent_Version_2(nums, k) :
    num_dict = defaultdict(int)

    for num in nums:
        num_dict[num] = num_dict[num] + 1  # count frequency

    length_dict = len(num_dict)

    temp_array = [0] * (length_dict + 2)
    # Here we need to handle the case when
    # x = [1,2] => dict = {1:1, 2:1} 1 and 2 both are repeated once
    for key, value in num_dict.items():
        if temp_array[value] == 0:
            temp_array[value] = [key]
        else:
            temp_array[value].append(key)

    result = []

    top = 0
    for num in temp_array[::-1]:
        if num != 0 and top != k:
            result.append(num)
            top = top + 1
    flattened_list = []
    for item_list in result:
        if isinstance(item_list, list):
            for item in item_list:
                flattened_list.append(item)
    return flattened_list

# if __name__ == "__main__":
#     # nums = [1,1,1,2,2,3]
#     # k = 2 # top 2 elements
#     # result = topKFrequent(nums, k)
#     # # Result will be like [0, [2], [1,2]]
#     # print(result)
#
#     nums = [1,2]
#     k = 2 # top 2 elements
#     result = topKFrequent_Version_2(nums, k)
#     print(result)