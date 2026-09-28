# Room to Grow

## Story

PyConES 2026 is getting bigger.

Much bigger.

The organising team has started preparing the conference rooms, but there is a small problem: every time a room reaches its maximum capacity, the team can **double** the number of available seats.

The first room starts with **1 seat**.

After one expansion, it has 2 seats.

After two expansions, it has 4 seats.

After three expansions, it has 8 seats.

And so on...

One of the organisers looks at the spreadsheet and says:

> *"We have the number of expansions, but nobody calculated the final capacity!"*

Another person opens their Python editor.

> *"Don't worry. This sounds like a job for Python."*

Your task is to calculate how many seats the room will have after a given number of expansions.

## Problem Statement

Given an integer `n`, calculate the number of seats available after performing `n` expansions.

The room starts with **1 seat**, and each expansion **doubles** its capacity.

## Input Format

A single line containing an integer:

```text
n
```

## Constraints

- `0 ≤ n ≤ 30`

## Output Format

A single integer representing the number of seats available after `n` expansions.