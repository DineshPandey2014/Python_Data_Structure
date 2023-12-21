"""
Iterative loop
"""
def square(num):
    while num > 0:
        print(num * num)
        num = num -1


if __name__ == "__main__":
    square(5)
