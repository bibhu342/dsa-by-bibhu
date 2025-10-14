# -----------------------------------
# Step 1: Define Functions
# -----------------------------------

def gcd(a, b):
    """Return the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return the Least Common Multiple (LCM) of two numbers using GCD."""
    return (a * b) // gcd(a, b)

def reverse_string(s):
    """Return the reversed string using a loop."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# -----------------------------------
# Step 2: Main Function
# -----------------------------------

def main():
    # Get numbers from user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Display GCD and LCM
    print("GCD:", gcd(a, b))
    print("LCM:", lcm(a, b))

    # Get string from user
    s = input("Enter a string: ")

    # Display reversed string using both methods
    print("Reversed (Loop):", reverse_string(s))
    print("Reversed (Slicing):", s[::-1])

# -----------------------------------
# Step 3: Execution Guard
# -----------------------------------

if __name__ == "__main__":
    main()
