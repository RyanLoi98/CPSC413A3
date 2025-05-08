## Optimal Coin Game

![Coin Game Example](https://imgur.com/mpHPT1q.png)


This is my CPSC 413 (Design and Analysis of Algorithms I - Winter 2024) assignment 3 question #3 at the University of Calgary.

This Program implements a dynamic programming solution to the classic two-player optimal coin-picking game. Given an array of coin values, this Python 3 program determines the best strategy for the current player to maximize their winnings assuming both players play optimally.

The core logic is implemented in the `Game` class using memoization to avoid redundant subproblem calculations. The function returns three key pieces of information: the maximum sum the current player can achieve, the margin of victory (or loss), and whether the optimal first move is to take the coin on the left or the right.

---

### Problem Description:

Given a list of positive integer coin values and two indices `start` and `end`, the function determines:

* `max`: The maximum sum the current player can collect from the coins between indices `start` and `end`, inclusive.
* `margin`: The margin by which the current player wins or loses, assuming both players play optimally.
* `takeRight`: A boolean indicating whether the player should take the coin on the right (`True`) or the left (`False`) to achieve the optimal outcome. If both moves result in the same value, the function defaults to choosing the right.

This solution uses a top-down recursive approach with memoization via a 2D data structure to store intermediate results for overlapping subproblems.

---

### Sample Usage:

```python
coingame = Game([4, 4, 9, 4, 1, 2, 3])
print(coingame.run(0, 3))  # Output: (13, 5, False)
print(coingame.run(2, 2))  # Output: (9, 9, True)
```

---

### Features:

* Optimized recursive dynamic programming with memoization
* Efficient handling of overlapping subproblems
* Returns full strategy insight: value, margin, and move
* Handles edge cases (invalid indices, empty list, one coin, etc.)

---

### Technologies:

* Python 3
* No external dependencies

---

### Educational Value:

This project demonstrates the application of dynamic programming techniques and game theory principles to develop an optimal solution for a competitive decision-making problem. The problem and its solution are inspired by topics in algorithm design, recursion, and optimal substructure.

---

Thanks! Based on your updated code structure, here’s a corrected and polished version of the **usage instructions** for your **coin game** program:

---

### **Usage Instructions for the Coin Game Program**

To use this program:

1. **Create a Python 3 File**
   Write a separate Python script that:

   * Imports or includes the `Game` class from `coinGame.py`.
   * Instantiates the `Game` class with a list of coin values.
   * Calls the `run(start, end)` method with a specific subrange of the coins.

   #### Example:

   ```python
   from coinGame import Game

   coingame = Game([4, 4, 9, 4, 1, 2, 3])
   print(coingame.run(0, 3))  # (13, 5, False)
   print(coingame.run(0, 4))  # (12, 2, False)
   print(coingame.run(2, 2))  # (9, 9, True)
   print(coingame.run(4, 6))  # (4, 2, True)
   ```


2. **How to Run**
   Save your test script (e.g., `test_game.py`) in the same directory as `coinGame.py`, and run:

   ```bash
   python3 test_game.py
   ```

3. **Alternatively**

    Alternatively you could use the included script that I provided called `a3test.py` to test this program. 
    To run this script you would enter this command into the terminal:

    ```bash
   python3 a3test.py
   ```