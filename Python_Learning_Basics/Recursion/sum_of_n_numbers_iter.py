"""
Recursive sum of n numbers
"""

def sum_of_n(num):
    if num == 0:
        return 0
    return sum_of_n(num-1) + num


if __name__ == "__main__":
    print(sum_of_n(4));
