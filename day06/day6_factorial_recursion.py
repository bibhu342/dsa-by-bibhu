def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    Time Complexity:
        O(n): One recursive call per decrement.
    Space Complexity:
        O(n): Due to recursion stack.
"""
    if n < 0:
        raise ValueError("Number can not be negative")
    if n == 0:
        return 1
    if n > 0:
        return n * factorial(n-1)
    
def main():
    test_cases = [

        10,
        0,
        1,
        -5          # Edge case: Raise value Error
    ]

    for num in test_cases:
        try:
            print(f"Factorial is: ", factorial(num))
        except ValueError as e:
            print(f"ValueError: cannot compute factorial for {num} ->", e)

if __name__ == "__main__":
    main()