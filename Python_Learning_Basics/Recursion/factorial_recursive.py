def factorial_recursive(num):
    if num == 0:
        return 1

    return factorial_recursive(num-1) * num

if __name__ == "__main__":
    result = factorial_recursive(6)
    print(result)

