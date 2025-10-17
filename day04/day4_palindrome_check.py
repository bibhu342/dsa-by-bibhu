# -----------------------------------------------------------
# Problem: Palindrome — Check if a given string is a palindrome.
# -----------------------------------------------------------
# Approach:
# 1. Normalize the string (remove spaces, make lowercase).
# 2. Compare the string with its reverse (slicing) OR
# 3. Use two-pointer method to compare characters from both ends.
#
# Edge Cases:
# - Empty string → True (considered palindrome).
# - Strings with spaces and mixed case ("Nurses Run").
# - Single character → True.
# - Optional: Handle punctuation (e.g., "A man, a plan, a canal: Panama").
# -----------------------------------------------------------


# *** Method 1: Using Slicing (Simple) ***
def is_palindrome_slicing(s: str) -> bool:
    """
    Check if the given string is a palindrome using slicing.

    Args:
        s (str): Input string.

    Returns:
        bool: True if s is palindrome, else False.

    Time Complexity:
        O(n) - create reversed copy and compare.
    Space Complexity:
        O(n) - due to reversed string creation.
    """
    # Step 1: Normalize the string (remove spaces and lowercase)
    s = s.replace(" ", "").lower()

    # Step 2: Compare original with reversed
    return s == s[::-1]


# *** Method 2: Two-pointer (Optimized + Interview Style) ***
def is_palindrome_two_pointer(s: str) -> bool:
    """
    Check if the given string is a palindrome using two-pointer approach.

    Args:
        s (str): Input string.

    Returns:
        bool: True if s is palindrome, else False.

    Time Complexity:
        O(n) — single pass from both ends.
    Space Complexity:
        O(1) — only pointers are used.
    """
    # Step 1: Normalize string
    s = s.replace(" ", "").lower()

    # Step 2: Initialize pointers
    left, right = 0, len(s) - 1

    # Step 3: Move pointers inward
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    # Step 4: If loop finishes without mismatch, it's a palindrome
    return True


# -----------------------------------------------------------
# Test cases for both methods
# -----------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ("madam", True),                # simple palindrome
        ("Nurses Run", True),           # spaces + mixed case
        ("hello", False),               # non-palindrome
        ("", True),                     # empty string
        ("a", True),                    # single character
    ]

    print("---- Testing Slicing Method ----")
    for s, expected in test_cases:
        result = is_palindrome_slicing(s)
        print(f"Input: '{s}' → {result} (Expected: {expected})")

    print("\n---- Testing Two-pointer Method ----")
    for s, expected in test_cases:
        result = is_palindrome_two_pointer(s)
        print(f"Input: '{s}' → {result} (Expected: {expected})")


"""
-----------------------------------------------------------
Final Explanation:

We need to check whether a given string is a palindrome.

1. Slicing Method (Brute force):
   - Reverse the string using s[::-1] and compare it with the original.
   - Simpler to implement but creates a reversed copy → O(n) space.

2. Two-pointer Method (Optimized):
   - Start with pointers at both ends.
   - Compare characters while moving inward.
   - If mismatch → return False. If loop ends → palindrome.
   - O(n) time, O(1) space.

We also normalize input (remove spaces, lowercase) so:
- "Nurses Run" → "nursesrun"
- Edge cases (empty string, single char) are naturally handled.

This makes it an ideal **interview-ready solution**.
-----------------------------------------------------------
"""
