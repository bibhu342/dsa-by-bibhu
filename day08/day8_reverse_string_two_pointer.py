# -----------------------------------------------------------
# Problem: Reverse String — Two Pointer Approach
# -----------------------------------------------------------
# Approach:
# 1. Input Validation:
#       - Input must be a list of single-character strings (e.g., ['B', 'i', 'b', 'h', 'u']).
#       - Raise TypeError if input is not a list or contains non-string elements.
# 2. Initialize Two Pointers:
#       - left = 0
#       - right = len(s) - 1
# 3. Swap Elements:
#       - While left < right:
#           s[left], s[right] = s[right], s[left]
#           left += 1
#           right -= 1
# 4. No return required — reversal happens in place.
# -----------------------------------------------------------

def reverse_string_in_place(s: list[str]) -> None:
    """
    Reverse a list of characters in place using the two-pointer technique.

    Args:
        s (list[str]): A list of single-character strings to be reversed.

    Raises:
        TypeError: If s is not a list, or contains non-string elements.

    Time Complexity:
        O(n) — where n is the length of the list.
    Space Complexity:
        O(1) — in-place reversal.
    """
    # Input validation
    if not isinstance(s, list):
        raise TypeError("Input must be a list of characters")
    if any(not isinstance(ch, str) or len(ch) != 1 for ch in s):
        raise TypeError("All elements must be single-character strings")

    # Two-pointer reversal
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def main() -> None:
    """
    Test driver for reverse_string_in_place().
    """
    test_cases = [
        list("Bibhu"),
        list("hello"),
        list("A"),
        [],
        ["B", 2, "C"],  # invalid element
        "notalist"      # invalid type
    ]

    print("---- Testing Reverse String (Two Pointer) ----\n")
    for s in test_cases:
        try:
            print(f"Original: {s}")
            reverse_string_in_place(s)
            print(f"[PASS] Reversed: {s}\n")
        except Exception as e:
            print(f"[ERROR] reverse_string_in_place({s}) -> {type(e).__name__}: {e}\n")


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------------
Final Explanation:
-----------------------------------------------------------

1. Two-Pointer Logic:
   - Start with left at the beginning and right at the end.
   - Swap characters at these pointers, then move inward.
   - Stop when left >= right.

2. Input Validation:
   - Ensure s is a list of single-character strings.
   - Raise errors for invalid inputs to avoid runtime issues.

3. Edge Cases:
   - Empty list → remains empty.
   - Single-character list → unchanged.
   - Invalid types raise TypeError.

4. Complexity:
   - Time: O(n) because we loop through the list once.
   - Space: O(1) because reversal is done in place without extra memory.

✅ Example Trace:
s = ['B','i','b','h','u']
left=0, right=4 → swap → ['u','i','b','h','B']
left=1, right=3 → swap → ['u','h','b','i','B']
left=2, right=2 → stop

Result: ['u','h','b','i','B']

-----------------------------------------------------------
Expected Output:
-----------------------------------------------------------
Original: ['B', 'i', 'b', 'h', 'u']
[PASS] Reversed: ['u', 'h', 'b', 'i', 'B']

Original: ['h', 'e', 'l', 'l', 'o']
[PASS] Reversed: ['o', 'l', 'l', 'e', 'h']

Original: ['A']
[PASS] Reversed: ['A']

Original: []
[PASS] Reversed: []

Original: ['B', 2, 'C']
[ERROR] reverse_string_in_place(['B', 2, 'C']) -> TypeError: All elements must be single-character strings

Original: notalist
[ERROR] reverse_string_in_place(notalist) -> TypeError: Input must be a list of characters
-----------------------------------------------------------
"""
