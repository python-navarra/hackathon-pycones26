# Py-Con-currency Issues II

You came as a big group from your local Python association — the regulars,
the Thursday meetup crowd, the ones who argue in the Telegram group chat
about whether `black` or `ruff` is the better formatter. You all arrived in
Barcelona together, on the same train, singing the "import antigravity" song
in the next carriage over without anyone asking you to.

But on Saturday morning, standing in front of the schedule grid, someone
says it out loud:

—"If we split up, we could see all of them."

Silence. Knowing looks. Someone is already doing mental math and failing
spectacularly.

—"Okay, but... how many of us would that actually take?"

That's the real problem: you don't want to miss a single talk of the day,
but you also don't want to drag half the conference along with you if fewer
people could already cover everything. You need the **minimum** number of
people from the group so that, splitting up, every talk has at least one
friend sitting in the room.

You open your laptop. Again.

## Problem Statement

You are given the schedule of all the talks for one day of PyConES: for each
talk, its **start** and **end** time (in minutes since the start of the
day, as integers).

Each person in the group can only be in one room at a time: if two talks
overlap, they need two different people to cover them. Two talks are
considered to **overlap** if one starts before the other ends (if a talk
ends exactly when another one starts, the same person can move straight
from one to the other, no extra person needed).

Write a Python program that calculates the **minimum number of people**
needed so the group can attend every talk of the day, without missing any
of them.

## Input Format

- The first line contains an integer `n`, the number of talks.
- Each of the following `n` lines contains two integers `start` and `end`,
  separated by a space.

## Constraints

```
1 ≤ n ≤ 10^5
0 ≤ start < end ≤ 10^4
```

## Output Format

A single integer: the minimum number of people required.

## Sample Input 0

```
6
0 30
25 60
40 70
50 90
80 90
90 120
```

## Sample Output 0

```
3
```

## Explanation 0

Right before minute 60, the following talks are simultaneously active: `(25,60)`, `(40,70)`, and `(50,90)` — 3 overlapping talks at once. At no other point in the day are there more than 3 active talks simultaneously, so 3 people are both necessary and sufficient to cover the whole day.