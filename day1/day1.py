#!/usr/bin/env python3

# input.txt: 1152
# example.txt: 3

import sys
import operator
from itertools import accumulate

def process_loop(lines):
    dial = 50
    password = 0
    rotations = [(l[0], int(l[1:])) for l in lines]

    for (dir, distance) in rotations:
        if dir == "L":
            distance *= -1
        dial += distance
        if dial % 100 == 0:
            password += 1

    return password

def process_func(lines):
    sign = {"L": 1, "R": -1}
    rotations = [int(l[1:]) * sign[l[0]] for l in lines]        
    dials = accumulate(rotations, operator.add, initial=50)

    return sum(1 for d in dials if d % 100 == 0)

def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input-file> <expected>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        expected = int(sys.argv[2])
        actual = process_func(f.read().splitlines())

        assert actual == expected, f"Expected {expected}, got {actual}"
        print(f"Success: {expected}")

if __name__ == "__main__":
    main()