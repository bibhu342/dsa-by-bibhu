from typing import List, Tuple

def max_water(nums: List[int]) -> int:
    """
    Find the maximum area formed between two lines in nums.
    Uses the two-pointer technique.
    """
    n = len(nums)
    if n < 2:
        return 0

    left = 0
    right = n - 1
    max_area = 0

    while left < right:
        # Calculate the width between two lines
        width = right - left
        # Determine the smaller height and calculate current area
        curr_area = min(nums[left], nums[right]) * width

        # Update max_area if a larger area is found
        if curr_area > max_area:
            max_area = curr_area

        # Move the pointer that points to the shorter line
        # This helps potentially find a taller line and a bigger area
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
        else:
            # If both heights are equal, move any pointer (left here)
            left += 1

    return max_area


def max_water_with_best_pairs(nums: List[int]) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Find the maximum area and list of pairs (indices) that form that area.

    Returns:
        max_area: the maximum water area found
        best_pairs: list of (left, right) index pairs achieving max_area
    """
    n = len(nums)
    if n < 2:
        return 0, []

    left = 0
    right = n - 1
    max_area = 0
    best_pairs: List[Tuple[int, int]] = []

    while left < right:
        # Calculate the width and area
        width = right - left
        curr_area = min(nums[left], nums[right]) * width

        # If we find a new larger area, reset best_pairs
        if curr_area > max_area:
            max_area = curr_area
            best_pairs = [(left, right)]
        elif curr_area == max_area:
            # If area ties with max, add the pair to the list
            best_pairs.append((left, right))

        # Move pointers based on shorter height to explore better options
        if nums[left] < nums[right]:
            left += 1
        elif nums[left] > nums[right]:
            right -= 1
        else:
            left += 1

    return max_area, best_pairs


# Example usage and test cases
if __name__ == "__main__":
    test_cases = [
        [],  # empty input
        [5],  # single element
        [1, 2],  # minimal valid case
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # classic example
        [1, 2, 3, 4, 5, 6],  # increasing heights
        [6, 5, 4, 3, 2, 1],  # decreasing heights
        [1, 8, 6, 2, 5, 4, 8, 3, 7, 8],  # extra tall end
        [1, 1, 1, 1, 1],  # flat heights
        [2, 3, 10, 5, 7, 8, 9],  # varied heights
    ]

    for arr in test_cases:
        print("Input:", arr)
        area = max_water(arr)
        print("Max Area (only):", area)
        print("-" * 20)
        area, pairs = max_water_with_best_pairs(arr)
        print("Max Area (with pairs):", area)
        print("Best Pairs (0-based):", pairs)
        print("Best Pairs (1-based):", [(l + 1, r + 1) for l, r in pairs])
        print("-" * 50)
