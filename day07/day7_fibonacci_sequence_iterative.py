# -----------------------------------------------------------
# Problem: Fibonacci Sequence — Return the first N Fibonacci numbers
# -----------------------------------------------------------
# Approach:
# 1. Validate input:
#       - Must be non-negative integer
#       - Negative → raise ValueError
#       - Non-integer → raise TypeError
# 2. Handle base cases:
#       - n = 0 → []
#       - n = 1 → [0]
# 3. Build the sequence iteratively:
#       - Start with [0, 1]
#       - Loop from 2 to n-1
#       - Append the sum of the last two numbers
# -----------------------------------------------------------

def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate a list containing the first n Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci terms to generate.

    Returns:
        list[int]: A list of the first n Fibonacci numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Time Complexity:
        O(n) — one loop through n elements.
    Space Complexity:
        O(n) — storing the sequence in a list.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Number cannot be negative.")

    # Base cases
    if n == 0:
        return []
    if n == 1:
        return [0]

    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Build the sequence iteratively
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence


def main() -> None:
    """
    Simple test driver for fibonacci_sequence().
    """
    test_cases = [0, 1, 2, 5, 10, -3, 7.5]

    print("---- Testing Fibonacci Sequence ----\n")
    for num in test_cases:
        try:
            result = fibonacci_sequence(num)
            print(f"[PASS] fibonacci_sequence({num}) = {result}")
        except Exception as e:
            print(f"[ERROR] fibonacci_sequence({num}) -> {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------------
Final Explanation:
-----------------------------------------------------------

We generate a Fibonacci sequence up to N terms.

1. Mathematical Definition:
   F(0) = 0
   F(1) = 1
   F(n) = F(n-1) + F(n-2)

2. Logic:
   - For n=0 → []
   - For n=1 → [0]
   - For n>=2 → build iteratively by summing the last two numbers

3. Input Validation:
   - Raise TypeError if n is not int
   - Raise ValueError if n < 0

4. Edge Cases:
   fibonacci_sequence(0) = []
   fibonacci_sequence(1) = [0]
   fibonacci_sequence(2) = [0, 1]
   fibonacci_sequence(5) = [0, 1, 1, 2, 3]
   fibonacci_sequence(-3) → ValueError
   fibonacci_sequence(7.5) → TypeError

5. Complexity:
   - Time: O(n)
   - Space: O(n)

✅ Example:
n = 5
Start [0, 1]
→ append 1 → [0, 1, 1]
→ append 2 → [0, 1, 1, 2]
→ append 3 → [0, 1, 1, 2, 3]
Result: [0, 1, 1, 2, 3]
-----------------------------------------------------------
"""
