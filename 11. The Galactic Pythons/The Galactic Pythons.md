## Story

The organizers of PyConES have prepared something special for this year's conference: a battle inspired by the **Galactic Wars**.

Two programs have been created specifically for the occasion. One runs on **Python 2**, and the other runs on **Python 3**.

Before the battle starts, the organizers place a line of energy crystals between the two programs. Each crystal has a certain value depending on how much energy it contains.

The programs take turns collecting crystals. On each turn, a program can only take the crystal at the **left or right end** of the line.

Of course, neither program wants to make things easy for the other one. Each of them knows the value of every remaining crystal and always chooses the move that leads to the best possible outcome.

The battle begins with Python 2.

Can you determine how much energy Python 2 can obtain compared to Python 3 if both programs play perfectly?

## Problem Statement

There are `N` crystals arranged in a line. Each crystal has an associated integer value.

Python 2 and Python 3 take turns choosing a crystal from either end of the line. The chosen crystal is removed and its value is added to the player's score.

Python 2 makes the first move, and both players play optimally.

Determine the **maximum score difference that Python 2 can guarantee** over Python 3.

## Input Format

The first line contains an integer `N`, representing the number of crystals.

The second line contains `N` integers representing the values of the crystals from left to right.

## Constraints

- `1 ≤ N ≤ 5000`
- `-10⁹ ≤ value of each crystal ≤ 10⁹`

## Output Format

Print the maximum difference between the score of Python 2 and the score of Python 3 that Python 2 can guarantee.