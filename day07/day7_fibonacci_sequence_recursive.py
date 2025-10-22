# -----------------------------------------------------------
# Problem: Fibonacci Sequence (Recursive) — Return the first N Fibonacci numbers
# -----------------------------------------------------------
# Approach:
# 1. Use recursion to build the sequence list step by step.
# 2. Base cases:
#       - n = 0 → []
#       - n = 1 → [0]
# 3. Recursive step:
#       - fibonacci_sequence(n) = fibonacci_sequence(n-1) + [fibonacci(n-1)]
# 4. fibonacci(n-1) is computed using a helper fibonacci() function.
# 5. Input validation prevents invalid types and negatives.
# -----------------------------------------------------------

def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number using recursion.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Number cannot be negative.")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(n: int) -> list[int]:
    """
    Generate the first n Fibonacci numbers using recursion.

    Args:
        n (int): Number of Fibonacci terms.

    Returns:
        list[int]: List of Fibonacci numbers from 0 to n-1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Time Complexity:
        O(n * 2^n) — because fibonacci(n) is called at each step.
    Space Complexity:
        O(n) — recursion call stack.
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

    # Recursive step
    return fibonacci_sequence(n - 1) + [fibonacci(n - 1)]


def main() -> None:
    """
    Simple test driver for fibonacci_sequence() recursive version.
    """
    test_cases = [0, 1, 5, 7, -2, 3.5]

    print("---- Testing Recursive Fibonacci Sequence ----\n")
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

1. We use recursion to build the sequence list.
   - Base:
        fibonacci_sequence(0) → []
        fibonacci_sequence(1) → [0]
   - Recursive:
        fibonacci_sequence(n) = fibonacci_sequence(n-1) + [fibonacci(n-1)]

2. fibonacci(n-1) is calculated using a helper recursive function fibonacci().

3. Input Validation:
   - Raise TypeError if not int
   - Raise ValueError if negative

4. Edge Cases:
   fibonacci_sequence(0) = []
   fibonacci_sequence(1) = [0]
   fibonacci_sequence(5) = [0, 1, 1, 2, 3]
   fibonacci_sequence(-2) → ValueError
   fibonacci_sequence(3.5) → TypeError

5. Complexity:
   - Time: O(n * 2^n) — inefficient because fibonacci() itself is exponential.
   - Space: O(n) — recursion stack.

✅ Example Trace:
fibonacci_sequence(4)
= fibonacci_sequence(3) + [fibonacci(3)]
= (fibonacci_sequence(2) + [fibonacci(2)]) + [2]
= ([0, 1] + [1]) + [2]
= [0, 1, 1, 2]
-----------------------------------------------------------
"""
