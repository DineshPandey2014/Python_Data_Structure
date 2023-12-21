def solution(a, k):
    result = [0 for _ in range(k)]
    res = 0
    for num in a:
        mod_value = num % k
        res += result[(k - mod_value) % k]
        result[mod_value] += 1
    return res

if __name__ == "__main__":
    a = [1,2,3,4,5]
    k = 2
    result = solution(a, k)
    print(result)



