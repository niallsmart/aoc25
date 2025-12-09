#!/usr/bin/env python3

# example.txt: 1227775554
# input.txt: 37314786486

import sys

def is_valid_id(id):
    chars = str(id)
    nchars = len(chars)
    for i in range(1, (nchars // 2) + 1):
        (d, m) = divmod(nchars, i)
        if m == 0 and (chars[0:i] * d) == chars:
            return False
    return True


def process(lines):
    ranges = lines[0].split(",")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    
    all = 0

    for start, end in ranges:
        all += sum(i for i in range(start, end + 1) if not is_valid_id(i))
 
    return all


def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input-file> <expected>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        expected = sys.argv[2]
        actual = str(process(f.read().splitlines()))

        assert actual == expected, f"Expected {expected}, got {actual}"
        print(f"Success: {expected}")

if __name__ == "__main__":
    main()