def solve(filename):
    """
    Solve the safe dial rotation puzzle.

    The dial has numbers 0-99 in a circle.
    Starting at 50, follow rotation instructions (L for left/lower, R for right/higher).
    Count how many times the dial points at 0 after any rotation.
    """
    position = 50
    zero_count = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Parse the rotation instruction
            direction = line[0]
            distance = int(line[1:])

            # Apply the rotation
            if direction == 'L':
                position = (position - distance) % 100
            else:  # direction == 'R'
                position = (position + distance) % 100

            # Check if we landed on 0
            if position == 0:
                zero_count += 1

    return zero_count


if __name__ == '__main__':
    result = solve('input.txt')
    print(f"The password is: {result}")
