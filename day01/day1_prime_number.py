# -----------------------------------------------
# Program: Prime Number Checker & Generator
# Author: Bibhudendu Behera
# Description:
#   This program checks whether a given number is prime
#   and also prints all prime numbers up to that number.
#   Time Complexity: O(√n)
# -----------------------------------------------

def is_prime(n: int) -> bool:

    """
    Check if a number is prime.
    Args:
        n (int): Number to check
    Returns:
        bool: True if prime, False otherwise
    """
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # Check divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) +1):
        # If divisible, then n is not prime
        if n % i == 0:
            return False
    # If no divisors found, n is prime
    return True

# ------------------ Main Execution ------------------

def main():

    # Take user input
    num = int(input("Enter a number:"))

    # Check if the entered number is prime
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not prime")

    # Print all prime numbers up to the entered number
    print(f"Prime numbers up to {num}:", end = " ")

    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end = " ")

    print()  # Ensures the cursor moves to a new line after printing primes

if __name__ == "__main__":
    main()

