# valid_palindrome.py
"""
DSA: String — Valid Palindrome (LeetCode #125 style)

Problem:
    Given a string s, return True if it is a palindrome after:
      - keeping only alphanumeric chars, and
      - ignoring case.

Examples:
    "A man, a plan, a canal: Panama" -> True
    "race a car"                     -> False
    ""                               -> True

Approaches:
1) Brute Force:
   - Normalize: keep only [a-z0-9], lowercase
   - Compare normalized string with its reverse
   Time:  O(n)
   Space: O(n)

2) Optimal (Two Pointers):
   - Use l, r indices; skip non-alnum; compare lowercase chars in-place
   Time:  O(n)
   Space: O(1)
"""

from typing import List


def is_palindrome_bruteforce(s: str) -> bool:
    """
    Normalize then compare to reverse.
    Time: O(n), Space: O(n)
    """
    norm = ''.join(ch.lower() for ch in s if ch.isalnum())
    return norm == norm[::-1]


def is_palindrome(s: str) -> bool:
    """
    Two-pointer in-place check (O(1) extra space).
    Time: O(n), Space: O(1)
    """
    l, r = 0, len(s) - 1
    while l < r:
        # Move left pointer to next alphanumeric
        while l < r and not s[l].isalnum():
            l += 1
        # Move right pointer to previous alphanumeric
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


# --- Optional: LeetCode-class wrapper for quick copy-paste ---
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# --- Minimal local tests (no external framework needed) ---
def _run_sanity_tests() -> None:
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".,,", True),
        ("0P", False),
        ("abba", True),
        ("ab@#Ba", True),
        ("", True),
    ]
    print("Sanity tests for valid_palindrome.py")
    for s, expected in cases:
        b = is_palindrome_bruteforce(s)
        o = is_palindrome(s)
        ok = (b == expected) and (o == expected)
        print(f"{s!r:35} -> brute={b}, optimal={o} | expected={expected} | {'OK' if ok else 'FAIL'}")


if __name__ == "__main__":
    _run_sanity_tests()
