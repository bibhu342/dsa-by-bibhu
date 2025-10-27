def reverse_string(s: str) -> str:
    """
    Reverse a given string using the Two Pointer technique.
    Time Complexity: O(n)
    Space Complexity: O(1) extra (in-place reversal)
    """

    # Convert the string into a list of characters because Python strings are immutable
    chars = list(s)

    # Initialize two pointers: one at the start, one at the end
    left = 0
    right = len(chars) - 1

    # Loop until the two pointers meet or cross
    while left < right:
        # Swap the characters at left and right
        chars[left], chars[right] = chars[right], chars[left]

        # Move the pointers inward
        left += 1
        right -= 1

    # Join the list back into a string and return the reversed result
    return ''.join(chars)


def main():
    """
    Test the reverse_string function with multiple test cases,
    including edge cases.
    """

    test_cases = [
        "Bibhu",       # normal string
        "",            # empty string
        "a",           # single character
        "racecar"      # palindrome
    ]

    for case in test_cases:
        result = reverse_string(case)
        print(f"Original: '{case}'  →  Reversed: '{result}'")


# Entry point to run the tests
if __name__ == "__main__":
    main()
