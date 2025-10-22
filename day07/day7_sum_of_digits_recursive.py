# -----------------------------------------------------------
# Problem: Sum of Digits — Compute the Sum of Digits of a Number Using Recursion
# -----------------------------------------------------------
# Approach:
# 1. Validate input:
#       - Must be a non-negative integer.
#       - If negative → raise ValueError
#       - If not an integer → raise TypeError
# 2. Base case:
#       - If n <= 9, return n (single-digit number).
# 3. Recursive case:
#       - sum_of_digits(n) = (n % 10) + sum_of_digits(n // 10)
#       - % extracts the last digit; // removes it.
# -----------------------------------------------------------

def sum_of_digits(n: int) -> int:
    """
    Compute the sum of digits of a non-negative integer using recursion.

    Args:
        n (int): Non-negative integer whose digits will be summed.

    Returns:
        int: Sum of digits of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Time Complexity:
        O(d) — where d is the number of digits in n.
    Space Complexity:
        O(d) — recursion call stack depth.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input cannot be negative")

    # Base case
    if n <= 9:
        return n

    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)


def main() -> None:
    """
    Test driver for sum_of_digits().
    """
    test_cases = [0, 5, 42, 1234, 99999, -10, 12.5]

    print("---- Testing Recursive Sum of Digits ----\n")
    for num in test_cases:
        try:
            result = sum_of_digits(num)
            print(f"[PASS] sum_of_digits({num}) = {result}")
        except Exception as e:
            print(f"[ERROR] sum_of_digits({num}) -> {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------------
Final Explanation:
-----------------------------------------------------------

1. Base Case:
   If n is a single-digit number (0-9), return n.

2. Recursive Case:
   sum_of_digits(n) = (n % 10) + sum_of_digits(n // 10)
   - n % 10 extracts the last digit.
   - n // 10 removes the last digit.
   Recursion continues until n becomes a single digit.

3. Input Validation:
   - Raise TypeError if n is not int
   - Raise ValueError if n is negative
   This ensures no infinite recursion or invalid operations.

4. Edge Cases:
   sum_of_digits(0) = 0
   sum_of_digits(5) = 5
   sum_of_digits(42) = 6
   sum_of_digits(1234) = 10
   sum_of_digits(99999) = 45
   sum_of_digits(-10) → ValueError
   sum_of_digits(12.5) → TypeError

5. Complexity:
   Time: O(d) where d is number of digits.
   Space: O(d) recursion stack.

✅ Example Trace:
sum_of_digits(123)
→ 3 + sum_of_digits(12)
→ 3 + (2 + sum_of_digits(1))
→ 3 + (2 + 1)
= 6

-----------------------------------------------------------
Expected Output:
-----------------------------------------------------------
[PASS] sum_of_digits(0) = 0
[PASS] sum_of_digits(5) = 5
[PASS] sum_of_digits(42) = 6
[PASS] sum_of_digits(1234) = 10
[PASS] sum_of_digits(99999) = 45
[ERROR] sum_of_digits(-10) -> ValueError: Input cannot be negative
[ERROR] sum_of_digits(12.5) -> TypeError: Input must be an integer
-----------------------------------------------------------
"""
