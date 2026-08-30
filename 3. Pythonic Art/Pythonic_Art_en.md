## Story

PyConES 2026 is not just code. It is also art.

The design team has decorated the entire venue with giant geometric shapes inspired by the logos of the most famous Python libraries. NumPy triangles. Pandas squares. Everywhere you look.

But just before the opening ceremony, the printing company calls with bad news: they have lost the exact measurements of each shape and need to recalculate the **perimeters** to know how much border material to purchase.

Luckily, someone saved a file with the name of each shape and its dimensions. All that is missing is the program to process it.

The editor is open. The supplier is waiting on the phone.

## Problem Statement

Given a geometric shape and its measurements, calculate its **perimeter**.

The possible shapes are:

- `triangle a b c` — triangle with sides **a**, **b** and **c**
- `square l` — square with side **l**

## Input Format

A single line with the name of the shape followed by its measurements:

```
shape measurement1 [measurement2] [measurement3]
```

If the shape is `square`, only one measurement is provided.
If the shape is `triangle`, three measurements are provided.

## Constraints

- The shape will always be one of: `triangle`, `square`
- All measurements are positive integers
- 1 ≤ measurements ≤ 1,000

## Output Format

A single integer with the perimeter of the shape.
