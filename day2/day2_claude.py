def is_invalid_id(num):
    """Check if a number is made of some sequence of digits repeated twice."""
    s = str(num)
    length = len(s)

    # The string must have even length to be repeated twice
    if length % 2 != 0:
        return False

    # Check if first half equals second half
    mid = length // 2
    return s[:mid] == s[mid:]


def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in a given range."""
    invalid_ids = []
    for num in range(start, end + 1):
        if is_invalid_id(num):
            invalid_ids.append(num)
    return invalid_ids


def solve(input_text):
    """Solve the gift shop problem."""
    # Parse the input - it's comma-separated ranges
    ranges_text = input_text.strip()
    range_parts = ranges_text.split(',')

    total = 0

    for range_part in range_parts:
        # Parse the range "start-end"
        start, end = map(int, range_part.split('-'))

        # Find invalid IDs in this range
        invalid_ids = find_invalid_ids_in_range(start, end)

        # Add them to the total
        total += sum(invalid_ids)

    return total


if __name__ == "__main__":
    # Read input
    with open("input.txt", "r") as f:
        input_text = f.read()

    # Solve and print result
    result = solve(input_text)
    print(f"Sum of all invalid IDs: {result}")
