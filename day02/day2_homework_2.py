# Problem: Reverse a given string
# Add edge cases + 2 more test cases per problem
# Reverse string solution without slicing.

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

def main():
    test_cases = [
        "Bibhu",                            # normal case    
        "",                                 # edge case: empty string
        "A man a plan a canal Panama",      # edge case: palindrome
        "hello world"                       # edge case: includes space
        "   ",                              # edge case: whitespace-only (added)
        "😊👍🏽"                             # edge case: unicode / emoji (added)
    ]

    for s in test_cases:
        print(f"Original: '{s}'")
        print(f"[Loop O(n)] → '{reverse_string_loop(s)}'")

if __name__ == "__main__":
    main()
