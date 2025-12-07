def find_max_joltage(bank):
    """Find the maximum joltage for a single battery bank.

    The joltage is formed by selecting any two digits in order.
    The resulting number uses the digits in the order they appear.

    Optimized O(n) solution:
    - For each position, we want to pair it with the maximum digit that comes after it
    - We scan from right to left, tracking the maximum digit seen so far
    """
    if len(bank) < 2:
        return 0

    n = len(bank)
    # Build array of maximum digit from each position to the end
    max_suffix = ['0'] * n
    max_suffix[-1] = bank[-1]

    for i in range(n - 2, -1, -1):
        max_suffix[i] = max(bank[i], max_suffix[i + 1])

    # Find the maximum joltage by pairing each digit with the max digit after it
    max_joltage = 0
    for i in range(n - 1):
        joltage = int(bank[i] + max_suffix[i + 1])
        max_joltage = max(max_joltage, joltage)

    return max_joltage


def solve(filename):
    """Solve the battery bank problem."""
    total_joltage = 0

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and line[0].isdigit():  # Only process lines that are battery banks
                max_joltage = find_max_joltage(line)
                total_joltage += max_joltage
                print(f"{line}: max joltage = {max_joltage}")

    return total_joltage


if __name__ == "__main__":
    # Test with the example from the problem
    example = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]

    print("Testing with example:")
    total = 0
    for bank in example:
        max_joltage = find_max_joltage(bank)
        total += max_joltage
        print(f"{bank}: {max_joltage}")
    print(f"Example total: {total}")
    print(f"Expected: 357")
    print()

    # Solve the actual puzzle
    print("Solving puzzle:")
    result = solve("input.txt")
    print(f"\nTotal output joltage: {result}")
