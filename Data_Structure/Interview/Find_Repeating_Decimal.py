def find_repeating_decimal(n, d):
    result = str(n // d)  # Integer part of the division
    remainder = n % d
    if remainder == 0:
        return result

    result += "."
    seen_remainders = {}
    while remainder != 0:
        if remainder in seen_remainders:
            non_repeating_part = result[:seen_remainders[remainder]]
            repeating_part = result[seen_remainders[remainder]:]
            return non_repeating_part + "(" + repeating_part + ")"

        seen_remainders[remainder] = len(result)
        remainder *= 10
        result += str(remainder // d)
        remainder %= d

    return result

if __name__ == "__main__":
    # Test cases
    print(find_repeating_decimal(1, 9))   # Output: "1"
    print(find_repeating_decimal(71, 70)) # Output: "142857"