# -----------------------------------------------------------
# Problem: Find the Second Largest Distinct Element in an Array
# -----------------------------------------------------------
# Approaches:
#   1️⃣ Sorting-based (Simple)         -> O(n log n) time, O(n) space
#   2️⃣ Single-pass (Optimized)        -> O(n) time, O(1) space
#
# Edge Cases:
#   - Empty or single-element list → raise ValueError
#   - All elements same → raise ValueError
# -----------------------------------------------------------


# -----------------------------------------------------------
# Approach 1: Sorting-based
# -----------------------------------------------------------
def second_largest_sort(nums: list[int]) -> int:
    """
    Find the second largest distinct element using sorting.
    """

    # Step 1: Remove duplicates
    unique_nums = list(set(nums))

    # Step 2: Check for at least two unique elements
    if len(unique_nums) < 2:
        raise ValueError("Array must have at least two distinct elements")

    # Step 3: Sort the list
    unique_nums.sort()

    # Step 4: Return second largest (second last element)
    return unique_nums[-2]


# -----------------------------------------------------------
# Approach 2: Single-pass (Optimized)
# -----------------------------------------------------------
def second_largest_single_pass(nums: list[int]) -> int:
    """
    Find the second largest distinct element in one pass.
    """

    # Step 1: Handle invalid cases
    if len(nums) < 2:
        raise ValueError("Array must have at least two elements")

    # Step 2: Initialize largest and second largest
    largest = second = float("-inf")

    # Step 3: Iterate through the list
    for num in nums:
        if num > largest:
            # Found a new largest
            second = largest
            largest = num
        elif largest > num > second:
            # Found a value between largest and second
            second = num

    # Step 4: Validate result
    if second == float("-inf"):
        raise ValueError("No second largest distinct element")

    # Step 5: Return result
    return second


# -----------------------------------------------------------
# Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([10, 5, 20, 8], 10),
        ([2, 2, 3, 1], 2),
        ([1, 2], 1),
        ([-5, -2, -9], -5),
    ]

    print("---- Sorting-based Results ----")
    for arr, expected in test_cases:
        try:
            print(f"{arr} -> {second_largest_sort(arr)} (Expected: {expected})")
        except ValueError as e:
            print(f"{arr} -> Error: {e}")

    print("\n---- Single-pass Results ----")
    for arr, expected in test_cases:
        try:
            print(f"{arr} -> {second_largest_single_pass(arr)} (Expected: {expected})")
        except ValueError as e:
            print(f"{arr} -> Error: {e}")


"""
We need the second largest DISTINCT value.

1) Sorting method:
   - Convert to set → remove duplicates.
   - Sort ascending → pick last-but-one.
   - Simple but O(n log n).

2) Single-pass method:
   - Track two variables: largest and second.
   - When we see a new number:
       a) If it's > largest, shift largest → second, update largest.
       b) Else if it's strictly between largest and second, update second.
   - Distinctness is ensured by the strict comparison (largest > x > second).
   - After one scan:
       - If 'second' never updated → no second largest distinct value.
       - Else return 'second'.

This yields O(n) time and O(1) space — preferred in interviews.
"""