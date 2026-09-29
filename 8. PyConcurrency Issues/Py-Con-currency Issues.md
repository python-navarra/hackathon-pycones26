# Py-Con-currency Issues

The first day of PyConES 2026 went perfectly. The welcome program printed
without a single bug, the opening keynote started right on time, and everyone
already has their badge hanging from the official lanyard.

But now comes the real challenge of the conference: **the schedule grid**.

There are five parallel rooms. And it's not like there are only a few options,
no. Just in one Saturday afternoon slot, you'd have to choose between "Lazy
imports and the art of interpreter procrastination," "Odyssey: From
Contributor to Maintainer," "Can AI Build an Integration on Its Own? The
Good, the Bad, and the Ugly," "Untangling the Web: Alternative Protocols
with Python," "Tachyon: Python 3.15's Sampling Profiler is Faster Than Your
Code," and "What Comes After Rust in the Python Ecosystem?" — and that's
not even counting the other forty-something talks happening the rest of the
weekend.

You want to see them all. Physically, you can't: if two talks overlap even
by a minute, you have to pick one. And as a good pythonista, you're not
going to decide "by eye" — you're going to write code to solve it.

Someone from the staff approaches you, looking a bit anxious:

—"Hey, you're the one who codes, right? We need to know, for the conference
stats, what's the **maximum number of talks a single person could attend**
today, without any of them overlapping."

You open your editor. You already know what's coming.

## Problem Statement

You are given the schedule of all the talks for one day of PyConES: for each
talk, its **start** and **end** time (in minutes since the start of the
day, as integers).

A person can attend a talk only if it doesn't overlap with any other talk
they've already decided to attend. Two talks are considered to **overlap**
if one starts before the other ends (if a talk ends exactly when another
one starts, they can be chained back-to-back — that is not considered an
overlap).

Write a Python program that calculates the **maximum number of talks** a
person can attend that day.

## Input Format

- The first line contains an integer `n`, the number of talks.
- Each of the following `n` lines contains two integers `start` and `end`,
  separated by a space, indicating the start and end minute of that talk.

## Constraints

```
1 ≤ n ≤ 10^5
0 ≤ start < end ≤ 10^4
```

## Output Format

A single integer: the maximum number of non-overlapping talks that can be
attended.

## Sample Input 0

```
6
0 30
25 60
40 70
50 90
80 100
90 120
```

## Sample Output 0

```
4
```

## Explanation 0

One optimal selection is: `(0,30)`, `(40,70)`, `(80,100)`, `(90,120)` → 4
non-overlapping talks. No combination allows attending 5 or more talks.
