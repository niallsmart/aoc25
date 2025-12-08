#!/usr/bin/env python3

# input.txt: 1152 / 6671
# example.txt: 3 / 6

import sys
import operator
import math
from itertools import accumulate


def process_part2_v1(lines):

    def turn_right(start, distance, collect = []):
        move = min(distance, 100 - start)
        start += move
        start %= 100
        distance -= move
        collect.append((start, move))
        if distance > 0:
            turn_right(start, distance, collect)

    def turn_left(start, distance, collect = []):
        if start == 0:
            move = min(distance, 100)
        else:
            move = min(distance, start)
        start -= move
        start %= 100
        distance -= move
        collect.append((start, move))
        if distance > 0:
            turn_left(start, distance, collect)


    rotations = [(l[0], int(l[1:])) for l in lines]        
    position = 50
    password = 0
    
    for (dir, distance) in rotations:
        turns = []
        if dir == 'L':
            turn_left(position, distance, turns)
        else:
            turn_right(position, distance, turns)

        password += sum(1 for s, _ in turns if s == 0)
        position = turns[-1][0]

    return password


def process_part2_v2(lines):
    rotations = [(l[0], int(l[1:])) for l in lines]        
    position = 50
    password = 0
    
    for (dir, distance) in rotations:

        password += distance // 100
        rem = distance % 100

        if dir == 'L':
            position -= rem
            if position <= 0 and (position + rem) > 0:
                password += 1 
        else:
            position += rem
            if position >= 100:
                password += 1 

        position %= 100


    return password

def process_part1(lines):
    sign = {"L": -1, "R": +1}
    rotations = [int(l[1:]) * sign[l[0]] for l in lines]        
    dials = accumulate(rotations, operator.add, initial=50)

    return sum(1 for d in dials if d % 100 == 0)

def main():
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input-file> <expected>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        expected = int(sys.argv[2])
        actual = process_part2_v2(f.read().splitlines())

        assert actual == expected, f"Expected {expected}, got {actual}"
        print(f"Success: {expected}")

if __name__ == "__main__":
    main()

