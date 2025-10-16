# Find max in array
# Add edge cases + 2 more test cases per problem.

def find_max(arr: list[int]) -> int:
    """
        Find and return the largest element in the list
        Args:
            arr: list[int]: A list of integers
        Returns:
            largest element in the list
        Raises:
            raise ValueError if the sring is empthy
        Time Complexity:
            O(n): One full pass through the list
        Space Complexity:
            O(1): Constant space used
    """

    if not arr:
        raise ValueError("Array must not be empty")
    
    max_value = arr[0]

    for num in arr[1:]:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == "__main__":
    test_cases = [
        [],                             # empty string                  
        [-1, -9, 3, 9],                 # +ve and -ve integers            
        [i for i in range(100)],        # inside list        
        [7, 7, 7, 6]                     # duplicates    
    ]

    for arr in test_cases:
        try:
            print(f"Array: {arr} -> Largest: {find_max(arr)}")
        except ValueError as e:
            print(f"Array: {arr} -> Error: {e}")