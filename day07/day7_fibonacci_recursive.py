# -----------------------------------------------------------
# Problem: Fibonacci — Compute the nth Fibonacci Number Using Recursion
# -----------------------------------------------------------
# Approach:
# 1. Use recursion based on the mathematical definition:
#       - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
#       - Base cases:
#           fibonacci(0) = 0
#           fibonacci(1) = 1
# 2. Validate input:
#       - Must be a non-negative integer.
#       - If negative → raise ValueError.
#       - If not an integer → raise TypeError.
# 3. Recursive calls continue until the base case is reached.
#
# Edge Cases:
# - n = 0 → returns 0
# - n = 1 → returns 1
# - n < 0 → raises ValueError
# - Non-integer inputs → raises TypeError
# - Very large n → recursion depth limit (≈1000 by default)
# -----------------------------------------------------------

def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Time Complexity:
        O(2^n) — exponential due to repeated subproblem computation.
    Space Complexity:
        O(n) — recursion call stack depth.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Number cannot be negative.")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    """
    Simple test driver for fibonacci().
    Uses try/except to show both valid outputs and validation errors cleanly.
    """
    test_cases = [
        0,     # base case
        1,     # base case
        5,     # small number
        10,    # larger number
        -3,    # invalid negative
        7.5,   # invalid non-integer
    ]

    print("---- Testing Recursive Fibonacci ----\n")
    for num in test_cases:
        try:
            result = fibonacci(num)
            print(f"[PASS] fibonacci({num}) = {result}")
        except Exception as e:
            print(f"[ERROR] fibonacci({num}) -> {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------------
Final Explanation:
-----------------------------------------------------------

We compute the nth Fibonacci number recursively.

1) Mathematical Definition:
   F(n) = F(n - 1) + F(n - 2)
   Base cases: F(0) = 0, F(1) = 1

2) Recursive Logic:
   - Each recursive call reduces n by 1 and by 2.
   - The base cases stop recursion and return fixed values (0 or 1).
   - Results bubble back up the call stack as sums.

3) Input Validation:
   - If n is not an integer → raise TypeError.
   - If n is negative → raise ValueError.
   - This prevents invalid or non-terminating recursion.

4) Edge Case Handling:
   - fibonacci(0) = 0
   - fibonacci(1) = 1
   - fibonacci(-3) → ValueError
   - fibonacci(7.5) → TypeError

5) Complexity:
   - Time: O(2^n)
   - Space: O(n)

✅ Example Trace:
fibonacci(4)
 → fibonacci(3) + fibonacci(2)
 → (fibonacci(2)+fibonacci(1)) + (fibonacci(1)+fibonacci(0))
 → ((fibonacci(1)+fibonacci(0))+1) + (1+0)
 → ((1+0)+1) + (1+0)
 = 3

-----------------------------------------------------------
Expected Output (for the provided tests):
-----------------------------------------------------------
[PASS] fibonacci(0) = 0
[PASS] fibonacci(1) = 1
[PASS] fibonacci(5) = 5
[PASS] fibonacci(10) = 55
[ERROR] fibonacci(-3) -> ValueError: Number cannot be negative.
[ERROR] fibonacci(7.5) -> TypeError: Input must be an integer.
-----------------------------------------------------------
"""
