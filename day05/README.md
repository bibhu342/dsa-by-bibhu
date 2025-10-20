\# 🐍 Day 05 — Two Sum Unique Pairs \& Gold Price Analysis



This folder contains two Python practice problems:

1\. \*\*DSA Problem:\*\* Two Sum — Unique Pairs  

2\. \*\*File Handling + Logic:\*\* Gold Price Analysis



---



\## 🧮 1. Two Sum — Unique Pairs (DSA)



\### 📌 Problem

Given an array of integers and a target value, return all \*\*unique pairs of numbers\*\* whose sum equals the target.



\### 🧠 Approach

\- Use a hash set `seen` to track visited numbers.

\- For each number:

&nbsp; - Compute complement = target - num

&nbsp; - If complement exists in `seen`, add the sorted pair to `pairs` set.

\- Convert set of tuples to list of lists for output.



\### ⚡ Complexity

\- Time: `O(n)`

\- Space: `O(n)`



\### 🧪 Example

```python

nums = \[1, 2, 3, 2, 4, -1]

target = 3

Output: \[\[1, 2], \[-1, 4]]


🪙 2. Gold Price Analysis (File + Logic)

📌 Problem



Read gold prices from prices.txt (one price per line) and calculate:



Minimum price



Maximum price



Average price



Up/Down days compared to previous day



🧠 Approach



Read file line by line and convert to floats



Use built-in min(), max(), sum() for stats



Loop through list to count up/down days



Print clean, structured results



⚡ Complexity



Time: O(n)



Space: O(n)



🧪 Example



prices.txt

2050.25

2051.50

2048.75

2052.00

2049.80


Output

📊 Gold Price Analysis Results

--------------------------------

📉 Min Price:       2048.75

📈 Max Price:       2052.00

📊 Average Price:   2050.46

⬆️  Up Days:         2

⬇️  Down Days:       2

🧮 Total Data Points: 5



🧰 File Structure

day05/

│── two\_sum\_unique\_pairs.py

│── gold\_price\_analysis.py

│── README.md

└── \_\_init\_\_.py

