# ---------------------------------------------
# Problem: Reverse a given string
# Approach:
#   1. Brute Force: Use a loop to build reversed string (O(n)).
#   2. Optimized: Use slicing to reverse in one line (O(n)).
# Edge Cases:
#   - Empty string ""
#   - Single character
#   - Palindrome (same forward and backward)
# ---------------------------------------------

'''# Basic Logic: Reverse a string using a loop
def reverse_string_basic(s):
    # Step 1: start with an empty string
    reversed_str = ""
    
    # Step 2: loop from last index to first index
    for i in range(len(s) - 1, -1, -1):
        reversed_str = reversed_str + s[i]  # append characters in reverse order
    
    # Step 3: return the reversed string
    return reversed_str


# --- Test code ---
input_str = "Bibhu"
print("Original:", input_str)
print("Reversed:", reverse_string_basic(input_str))
'''
# ---------------------------------------------

def reverse_string_loop(s: str) -> str:
    """
    Reverse a string using a manual loop.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def reverse_string_slice(s: str) -> str:
    """
    Reverse a string using Python slicing.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return s[::-1]


def main():
    # Test cases to verify correctness and edge handling
    test_cases = [
        "Bibhu",       # normal case
        "racecar",     # palindrome
        "",            # empty string
        "a",           # single character
        "hello world"  # includes space
    ]

    for s in test_cases:
        print(f"Original: '{s}'")
        print(f"[Loop O(n)] → '{reverse_string_loop(s)}'")
        print(f"[Slice O(n)] → '{reverse_string_slice(s)}'")
        print("---")


if __name__ == "__main__":
    main()
