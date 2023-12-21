"""
Iterative approach for factorial
Time Complexity is (n)
"""

def factorial(num):
    if num <= 0:
        return num
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result


if __name__ == "__main__":
    result = factorial(-1)
    print(result)
