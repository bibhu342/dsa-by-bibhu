# 📅 Day 1 — DSA Problem Set (Oct 14, 2025)

This folder contains Day 1 solutions for core Data Structures & Algorithms (DSA) problems implemented in Python.  
All problems are written with clean, modular code and structured for interview preparation.

---

## ✅ 1. Prime Number Checker & Generator

**File:** `day1_prime_number.py`  
- Check if a number is prime using an **O(√n)** primality test.
- Generate all prime numbers up to `N`.
- Efficient and beginner-friendly approach.

**Key Concepts:**  
- Looping up to √n for primality
- Efficient prime generation
- Handling edge cases for 0, 1, and negatives

---

## ✅ 2. GCD & LCM + String Reverse

**File:** `day1_gcd_lcm_reverse.py`  
- Compute **GCD** of two numbers using the **Euclidean algorithm**.
- Compute **LCM** using GCD.
- Reverse a string using:
  - Manual loop
  - Python slicing `[::-1]`

**Key Concepts:**  
- Euclidean GCD: O(log(min(a, b)))
- LCM via GCD formula: `LCM(a, b) = (a * b) // GCD(a, b)`
- String reversal methods

---

## ✅ 3. Sum of Numbers (Loop + Math Formula)

**File:** `day1_sum_of_number.py`  
- Calculate sum of numbers between `start` and `end` (inclusive).
- Brute-force loop (O(n)) and arithmetic series formula (O(1)).
- Clean, reusable function design.

**Key Concepts:**  
- Loops & accumulation
- Arithmetic series formula
- Edge case handling for negative numbers and swapped bounds

---

## 🧠 Skills Strengthened

- Mathematical problem solving
- Looping & conditionals
- Algorithmic thinking
- Clean coding structure for interviews

---

## 🏁 How to Run

```bash
python day1_prime_number.py
python day1_gcd_lcm_reverse.py
python day1_sum_of_number.py
```
