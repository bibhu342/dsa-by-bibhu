def reverse_integer(nums: int) -> int:

    """
        Return the integer formed by reversing its digits.
    Args:
        nums: int: Enter a number
    Returns:
        int: Reverse the digits of the numbers
    Raises:
        raise TypeError "Enter a number!"
    Time Complexity:
        O(n): One full cycle
    Space Complexity:
        O(1): One constant space

    """
    if not isinstance(nums, int):
        raise TypeError("Enter a number!")

    rev_num = 0
    sign = -1 if nums < 0 else 1
    nums = abs(nums)

    while nums > 0:
        digit = nums % 10
        rev_num = rev_num * 10 + digit
        nums //= 10
    return sign * rev_num

def main():

    test_cases = [
        1234, 
        100, 
        -121,
        0,             # Edge Case
        "Bibhu",       # Edge Case  Return TypeError
        ' '           # Edge Case: Retrun TypeError
    ]
        
    for num in test_cases:
        try:
            result = reverse_integer(num)
            print(f"Revrse integer of {num} is", result)
            
        except TypeError as e:
            print(f"Error for {num}: {e}")

if __name__ == "__main__":
    main()