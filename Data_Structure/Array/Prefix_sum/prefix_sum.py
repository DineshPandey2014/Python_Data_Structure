def answer_queries(nums, queries, limit):
    # Created prefix array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans

if __name__ == "__main__":
    nums = [1, 6, 3, 2, 7, 2]
    queries = [[0, 3], [2, 5], [2, 4]]
    limit = 13
    result = answer_queries(nums, queries, limit)
    print(result)




