# -----------------------------------------------------------
# Problem: Fibonacci with Memoization
# -----------------------------------------------------------
# Approach:
# 1. Use recursion + a memo dictionary to store computed values.
# 2. Check if the result for n exists in memo before computing.
# 3. Base cases:
#       fibonacci(0) = 0
#       fibonacci(1) = 1
# 4. Recursive case:
#       fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# 5. Memoization reduces complexity from O(2^n) to O(n).
# -----------------------------------------------------------

# Global memo dictionary to cache computed values
memo: dict[int, int] = {0: 0, 1: 1}


def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using recursion with memoization.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Time Complexity:
        O(n) — each Fibonacci number is computed once.
    Space Complexity:
        O(n) — memoization storage + recursion stack.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Number cannot be negative.")

    # Check memoized results
    if n in memo:
        return memo[n]

    # Recursive calculation and memoization
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def main() -> None:
    """
    Test driver for memoized fibonacci().
    """
    test_cases = [0, 1, 5, 10, 20, 30, -2, 5.5]

    print("---- Testing Memoized Recursive Fibonacci ----\n")
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

1. Naive recursion recomputes subproblems, making it O(2^n).
2. Memoization stores each computed Fibonacci number in a dictionary.
3. When a value is needed again, it's returned from the cache instantly.

For example:
f(10)
- f(9) + f(8)
- f(9) → f(8)+f(7)
- f(8) → already cached, instant return ✅

4. Edge Cases:
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(-2) → ValueError
fibonacci(5.5) → TypeError

5. Complexity:
- Time: O(n)
- Space: O(n)

✅ Example Output:
[PASS] fibonacci(0) = 0
[PASS] fibonacci(1) = 1
[PASS] fibonacci(5) = 5
[PASS] fibonacci(10) = 55
[PASS] fibonacci(20) = 6765
[PASS] fibonacci(30) = 832040
[ERROR] fibonacci(-2) -> ValueError: Number cannot be negative.
[ERROR] fibonacci(5.5) -> TypeError: Input must be an integer.
-----------------------------------------------------------
"""
