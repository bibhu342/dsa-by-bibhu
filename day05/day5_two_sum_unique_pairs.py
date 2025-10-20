# -----------------------------------------------------------
# Problem: Two Sum — Return All Unique Pairs That Sum to Target
# -----------------------------------------------------------
# Approach:
# 1. Use a hash set to store numbers we’ve already seen.
# 2. For each number:
#       - Compute complement = target - num
#       - If complement is already in the seen set → we found a pair.
#       - Sort the pair (to avoid (2,1) vs (1,2) duplication).
#       - Add the pair as a tuple to a set of pairs (to ensure uniqueness).
# 3. Convert the set of pairs to a list of lists for the final output.
#
# Edge Cases:
# - Empty list → return [].
# - Duplicates (e.g., [1, 2, 2, 3], target = 3) → only unique pairs returned.
# - Zeros and negatives handled naturally.
# - Multiple duplicates (e.g., [0,0,0,0], target = 0) → single pair [0,0].
# -----------------------------------------------------------


# *** Optimized Hash Set Method (Interview Style) ***
def two_sum_unique(nums: list[int], target: int) -> list[list[int]]:
    """
    Return all unique pairs of numbers that sum up to the given target.

    Args:
        nums (list[int]): Input list of integers.
        target (int): Target sum value.

    Returns:
        list[list[int]]: All unique pairs that sum to target.

    Time Complexity:
        O(n) — single pass, hash set lookup O(1).
    Space Complexity:
        O(n) — storing seen numbers and unique pairs.
    """
    seen = set()     # store numbers we've encountered
    pairs = set()    # store unique sorted pairs as tuples

    for num in nums:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    # convert set of tuples to list of lists
    return [list(pair) for pair in pairs]


# -----------------------------------------------------------
# Test cases
# -----------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 2, 4, -1], 3, [[1, 2], [-1, 4]]),  # duplicates + negative
        ([0, 0, 0, 0], 0, [[0, 0]]),                  # multiple zeros
        ([1, 1, 1, 1], 2, [[1, 1]]),                  # all same number
        ([-3, 3, -3, 3], 0, [[-3, 3]]),               # negatives
        ([], 5, []),                                  # empty input
    ]

    print("---- Testing Two Sum Unique Pairs ----")
    for nums, target, expected in test_cases:
        result = two_sum_unique(nums, target)
        print(f"nums={nums}, target={target} → {result} (Expected: {expected})")


"""
-----------------------------------------------------------
Final Explanation:

We need to return **unique pairs of values** whose sum equals the target.

1. Core Idea:
   - For each number in nums, compute complement = target - num.
   - If complement has already been seen, then (num, complement) is a valid pair.
   - Sort and store as a tuple in a set to ensure uniqueness.

2. Why sets?
   - `seen` allows O(1) lookup for complements.
   - `pairs` avoids duplicate pairs like [1,2] and [2,1].

3. Handling duplicates and zeros:
   - If the same number appears multiple times, it will only contribute once to the unique pairs.
   - Zero is treated like any other number.

4. Complexity:
   - Time: O(n)
   - Space: O(n)

✅ Example:
nums = [1, 2, 3, 2, 4, -1], target = 3
Iteration flow:
  seen={} → 1 seen
  complement for 2 = 1 → found pair (1,2)
  complement for 3 = 0 → no match
  second 2 ignored since 1 already matched
  complement for 4 = -1 → found pair (-1,4)

Final pairs: [[1, 2], [-1, 4]]
-----------------------------------------------------------
"""
