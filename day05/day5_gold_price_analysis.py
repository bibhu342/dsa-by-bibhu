# -----------------------------------------------------------
# Problem: Gold Price Analysis from Text File
# -----------------------------------------------------------
# Approach:
# 1. Read daily gold prices from `prices.txt` (one price per line).
# 2. Convert the string data to a list of floats.
# 3. Compute:
#       - Minimum price
#       - Maximum price
#       - Average price
# 4. Count:
#       - Number of days price went up (compared to previous day)
#       - Number of days price went down or stayed the same
# 5. Print the results in a clean format.
#
# Edge Cases:
# - Empty file → print message and exit.
# - Single price → no up/down day comparison.
# - Non-numeric lines → ignore or handle gracefully.
# -----------------------------------------------------------

from typing import List


def read_prices_from_file(filename: str) -> List[float]:
    """
    Reads gold prices from a file and returns a list of floats.
    Ignores empty or invalid lines.

    Args:
        filename (str): Path to the file.

    Returns:
        List[float]: List of price values.
    """
    prices = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                prices.append(float(line))
            except ValueError:
                print(f"⚠️ Skipping invalid line: {line}")
    return prices


def calculate_statistics(prices: List[float]) -> tuple:
    """
    Calculate min, max, and average price.

    Args:
        prices (List[float]): List of prices.

    Returns:
        tuple: (min_price, max_price, avg_price)
    """
    min_price = min(prices)
    max_price = max(prices)
    avg_price = sum(prices) / len(prices)
    return min_price, max_price, avg_price


def count_up_down_days(prices: List[float]) -> tuple:
    """
    Count how many days prices went up vs down.

    Args:
        prices (List[float]): List of prices.

    Returns:
        tuple: (up_days, down_days)
    """
    up_days = 0
    down_days = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            up_days += 1
        else:
            down_days += 1
    return up_days, down_days


def main():
    filename = "prices.txt"
    prices = read_prices_from_file(filename)

    if not prices:
        print(f"❌ No valid price data found in '{filename}'. Exiting.")
        return

    min_price, max_price, avg_price = calculate_statistics(prices)
    up_days, down_days = count_up_down_days(prices)

    print("\n📊 Gold Price Analysis Results")
    print("--------------------------------")
    print(f"📉 Min Price:       {min_price:.2f}")
    print(f"📈 Max Price:       {max_price:.2f}")
    print(f"📊 Average Price:   {avg_price:.2f}")
    print(f"⬆️  Up Days:         {up_days}")
    print(f"⬇️  Down Days:       {down_days}")
    print(f"🧮 Total Data Points: {len(prices)}")


if __name__ == "__main__":
    main()
