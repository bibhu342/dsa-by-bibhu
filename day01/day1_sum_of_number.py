# ---------------------------------------------
# Problem: Calculate the sum of numbers from start to end (inclusive).
# Approach:
#   1. Start with a simple loop (O(n) time) to build the logic clearly.
#   2. Then optimize using arithmetic series formula (O(1) time).
# Edge cases:
#   - If start > end → swap values.
#   - Handles negative numbers as well.
# ---------------------------------------------

def sum_range_loop(start: int, end: int) -> int:
    """
    Calculate sum of numbers from start to end using a loop.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if start > end:
        start, end = end, start  # swap if inputs are reversed
    total = 0
    for x in range(start, end + 1):
        total += x
    return total


def sum_range_math(start: int, end: int) -> int:
    """
    Calculate sum of numbers from start to end using arithmetic series formula.
    Sum = n * (first + last) / 2
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if start > end:
        start, end = end, start  # swap if inputs are reversed
    n = end - start + 1
    return n * (start + end) // 2  # integer division


def main():
    # Example inputs
    start = 1
    end = 10

    # 1. Brute Force - Loop based
    total_loop = sum_range_loop(start, end)
    print(f"[Loop O(n)] Sum of numbers from {start} to {end} = {total_loop}")

    # 2. Optimized - Math Formula
    total_math = sum_range_math(start, end)
    print(f"[Math O(1)] Sum of numbers from {start} to {end} = {total_math}")


if __name__ == "__main__":
    main()
