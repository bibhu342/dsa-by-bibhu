# ---------------------------------------------
# Problem: Find the maximum element in an array
# ---------------------------------------------
# Approach:
#   1. Initialize the first element as the current maximum.
#   2. Traverse the list once, comparing each element with the current maximum.
#   3. If any element is greater, update the current maximum.
# Edge Cases:
#   - Empty list → raise ValueError.
#   - All negative numbers.
#   - Duplicates or all equal values.
# ---------------------------------------------

# *** Basic Logic: Find maximum element using a loop
def find_max_basic(arr):
    # Step 1: start by assuming the first element is the max
    max_value = arr[0]

    # Step 2: loop through remaining elements
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]

    # Step 3: return the largest element
    return max_value


# --- Test code for basic logic ---
arr = [3, 7, 2, 9, 5]
print("Array:", arr)
print("Maximum element (Basic):", find_max_basic(arr))


# ---------------------------------------------
# Interview-Style Version (Optimized + Clean)
# ---------------------------------------------
def find_max(arr: list[int]) -> int:
    """
    Find and return the largest number in the list.

    Args:
        arr (list[int]): A list of integers (can include negative numbers).

    Returns:
        int: The largest integer in the list.

    Raises:
        ValueError: If the list is empty.

    Time Complexity:
        O(n) - one full pass through the list.
    Space Complexity:
        O(1) - constant space used.
    """

    # Step 1: handle edge case
    if not arr:
        raise ValueError("Array must not be empty")

    # Step 2: initialize max_value with the first element
    max_value = arr[0]

    # Step 3: scan through each element and update if larger
    for num in arr[1:]:
        if num > max_value:
            max_value = num

    # Step 4: return the final max value
    return max_value


# --- Test code for interview-style version ---
if __name__ == "__main__":
    test_cases = [
        [3, 7, 2, 9, 5],         # normal case
        [-10, -5, -30, -2],      # all negative
        [42],                    # single element
        [0, 0, 0, 0],            # all equal
        [5, 1, 5, 5, 2],         # duplicates
        []                       # empty (edge case)
    ]

    for arr in test_cases:
        try:
            print(f"Array: {arr} → Largest: {find_max(arr)}")
        except ValueError as e:
            print(f"Array: {arr} → Error: {e}")

        
'''We need to find the largest number in an array.
First, I handle the edge case by raising a ValueError if the array is empty.
Then I initialize the first element as my current maximum and use a for loop to scan through the rest of the elements.
If any element is larger, I update my max value.
This makes just one full pass, so the time complexity is O(n) and space is O(1).
Since I start with the first element, it also handles negative numbers and duplicates correctly.
'''



