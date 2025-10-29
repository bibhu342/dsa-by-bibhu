
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates in-place from a sorted list `nums`.
    Returns the length k of the array that contains unique elements in the first k positions.
    After the call, nums[:k] contains the unique elements in original order.
    """
    if not nums:
        return 0

    # slow pointer i points to index of last unique element
    i = 0
    for j in range(1, len(nums)):          # j scans through array
        if nums[j] != nums[i]:             # found next unique element
            i += 1
            nums[i] = nums[j]              # place it right after last unique
    return i + 1                           # length is index + 1


# Quick tests
if __name__ == "__main__":
    tests = [
        ([], 0),
        ([1], 1),
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),
        ([1,2,3,4], 4),
    ]

    for arr, expected_k in tests:
        a = arr.copy()
        k = remove_duplicates(a)
        print(f"input: {arr} | k={k} | uniques={a[:k]} | expected_k={expected_k}")
        assert k == expected_k, f"Expected {expected_k}, got {k}"
