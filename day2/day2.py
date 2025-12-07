#!/usr/bin/env python3

# example.txt: 1227775554
# input.txt: 37314786486

import sys

def is_valid_id(id):
    chars = str(id)
    nchars = len(chars) // 2
    return chars[0:nchars] != chars[nchars:]

def sum_invalid_ids(ranges):

    all = 0

    for start, end in ranges:
        all += sum(i for i in range(start, end + 1) if not is_valid_id(i))
 
    return all


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