
def findMaxConsecutiveOnes(self, nums) -> int:
    curr_max_consecutive_number = 0
    max_count = 0
    for num in nums:
        if num == 1:
            curr_max_consecutive_number = curr_max_consecutive_number + 1
            max_count = max(max_count, curr_max_consecutive_number)
        else:
            curr_max_consecutive_number = 0
    return max_count

