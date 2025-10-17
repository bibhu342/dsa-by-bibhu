# ---------------------------------------------
# Problem: Two Sum — Find indices of two numbers that add up to a target
# ---------------------------------------------
# Approach:
#   1. Use a hash map (dictionary) to store numbers we’ve already seen and their indices.
#   2. For each number in the array:
#        - Compute complement = target - num
#        - Check if complement is already in the map.
#        - If yes → return [index_of_complement, current_index].
#        - Else → store current number with its index.
# Edge Cases:
#   - Empty list → raise ValueError.
#   - No valid pair exists.
#   - Duplicates (e.g. [3, 3], target = 6).
#   - Negative numbers.
# ---------------------------------------------

# *** Basic Logic: Using two loops (brute force) ***
def two_sum_basic(nums: list[int], target: int) -> list[int]:
    # Step 1: check every pair
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # Step 2: if no pair found
    raise ValueError("No valid pair found")


# --- Test code for basic logic ---
nums = [2, 7, 11, 15]
target = 9
print("Nums:", nums, "Target:", target)
print("Two Sum (Basic):", two_sum_basic(nums, target))


# ---------------------------------------------
# Interview-Style Version (Optimized + Clean)
# ---------------------------------------------
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return indices of the two numbers such that they add up to target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target sum value.

    Returns:
        list[int]: Indices of the two numbers adding up to target.

    Raises:
        ValueError: If no valid pair exists.

    Time Complexity:
        O(n) - single pass through the list.
    Space Complexity:
        O(n) - worst case, storing all elements in hash map.
    """
    # Step 1: create empty dictionary to store number:index
    seen = {}

    # Step 2: iterate through the array
    for i, num in enumerate(nums):
        complement = target - num

        # Step 3: if complement already seen, return pair of indices
        if complement in seen:
            return [seen[complement], i]

        # Step 4: store current number and its index
        seen[num] = i

    # Step 5: if loop ends, no pair found
    raise ValueError("No valid pair found")


# --- Test code for interview-style version ---
if __name__ == "__main__":
    test_cases = [
        ([-3, 1, 2, 3], 0),      # negative + positive
        ([3, 3], 6),            # same number twice
        ([], 5),                # empty
        ([1, 2, 5, 7], 100),    # no valid pair
    ]

    for nums, target in test_cases:
        try:
            print(f"nums={nums}, target={target} → {two_sum(nums, target)}")
        except ValueError as e:
            print(f"nums={nums}, target={target} → Error: {e}")


'''
We need to find two numbers in the array that sum to a given target.
The brute force way checks every pair — O(n²) — but that’s slow.
The optimized solution uses a dictionary:
  - For each number, compute complement = target - num.
  - If complement already exists in the dictionary, we return the stored index and the current index.
  - Otherwise, we store num:index for future lookups.
This gives us O(n) time with O(n) space.
We handle edge cases explicitly: empty array or no valid pair raises ValueError.
'''
