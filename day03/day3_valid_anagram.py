# ---------------------------------------------
# Problem: Valid Anagram
# ---------------------------------------------
# Approach:
#   1. Normalize strings (remove spaces, lowercase).
#   2. If lengths differ → False.
#   3. Build frequency dict from s (increment).
#   4. Decrement using t; return False early on mismatch or negative count.
#   5. Confirm all counts are zero → True.
#
# Edge Cases:
#   - Empty strings -> True
#   - Different lengths -> False
#   - Works with any characters (letters, digits, symbols)
#   - Case-insensitive & space-agnostic by default here
#
# Time Complexity:  O(n)
# Space Complexity: O(k)
#-----------------------------------------------

def is_anagram(s: str, t: str) -> bool:
    # Step 1: Normalize (case-insensitive, ignore spaces)
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # Step 2: Early length check
    if len(s) != len(t):
        return False

    # Step 3: Build frequency map from s
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 4: Decrement using t with immediate checks
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    # Step 5: Final verification: all counts must be zero
    return all(v == 0 for v in freq.values())


# ----------------
# Quick tests
# ----------------
if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("", "") is True
    assert is_anagram("aabb!!", "!!baba") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("ab", "a") is False
    # Case-insensitive normalization example
    assert is_anagram("Listen", "Silent") is True
    print("All quick tests passed.")
