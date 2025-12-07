#!/usr/bin/env python3

# example.txt: 1227775554
# input.txt: 37314786486

import sys

def process(lines):
    return None

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

