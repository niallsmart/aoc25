#!/usr/bin/env python3

# example.txt: 357
# input.txt: 17405

import sys

def process(banks):
    total = 0
    for bank in banks:
        batteries = [int(b) for b in bank]
        bankmax = 0
        for i, bi in enumerate(batteries[:-1]):
            bi *= 10
            if bi > bankmax // 10:
                mbj = max(batteries[i + 1:])
                bankmax = max(bi + mbj, bankmax)
        total += bankmax
    return total


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

