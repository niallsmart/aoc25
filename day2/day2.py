#!/usr/bin/env python3

# example.txt: 3

import sys
import operator
from itertools import accumulate


def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

def is_valid_id(id):
    chars = str(id)
    nchars = len(chars)
    for d in divisors(nchars):
        if (chars[0:d] * int(nchars / d)) == chars:
            return False
    return True

def sum_invalid_ids(ranges):

    sum = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            if not is_valid_id(i):
                print(f"Invalid ID: {i}")
                sum += i
 
    return sum


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input-file> <expected>")
        sys.exit(1)

    with open(sys.argv[1]) as f:

        ranges = f.read().strip().split(",")
        ranges = [tuple(map(int, r.split("-"))) for r in ranges]

        actual = sum_invalid_ids(ranges)
        expected = sys.argv[2]

        assert actual == expected, f"Expected {expected}, got {actual}"
        print(f"Success: {expected}")


if __name__ == "__main__":
    main()