def valid_palindrome_II(s: str) -> bool:
    """
    Return True if s can be a palindrome after deleting at most one character.
    Time: O(n), Space: O(1)
    """

    def is_pal_range(s: str, i: int, j: int) -> bool:
        """Standard two-pointer palindrome check on s[i..j] inclusive."""
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1

    # Move inward until a mismatch or pointers cross
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # One delete allowed: skip left OR skip right
            skip_left  = is_pal_range(s, left + 1, right)
            skip_right = is_pal_range(s, left, right - 1)
            return skip_left or skip_right

    # No mismatches → already a palindrome
    return True


def main():
    test_cases = [
        "abca",      # True  (remove 'b' or 'c')
        "def",       # False
        "abccba",    # True  (already palindrome)
        "a",         # True
        "abc",       # False
        "deeee",     # True
        "abcdba",    # True  (remove 'c' or 'd')
    ]

    for s in test_cases:
        print(f"{s!r}: {valid_palindrome_II(s)}")


if __name__ == "__main__":
    main()
