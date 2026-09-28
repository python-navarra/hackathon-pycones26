In the central courtyard, two sound sources are competing with each other:
the main stage's PA system repeats an announcement every so many minutes,
and the workshop area's speaker repeats its own jingle, on its own cycle.
Both started playing at the exact same instant — the moment the conference
opened, minute 0 — but since their cycles are different, they almost never
line up again.

Almost. Someone on staff, who's been getting increasingly annoyed hearing
the two sounds overlap differently every time, finally asks the million
dollar question:

—"At what minute will they both start their cycle again **at the exact
same time**?"

Nobody wants to just sit there and wait to hear it by chance. Someone opens
their editor.

## Problem Statement

The main stage's announcement repeats every `a` minutes (it starts at
minute `0`, then `a`, then `2a`, and so on). The workshop area's jingle
repeats every `b` minutes (it starts at minute `0`, then `b`, `2b`, etc.).

Both started playing together at minute `0`. Calculate the **first minute
after 0** at which both start a new cycle at exactly the same time.

## Input Format

A single line containing two integers `a` and `b`, separated by a space.

## Constraints

```
1 ≤ a, b ≤ 1000
```

## Output Format

A single integer: the first minute (greater than 0) at which both cycles
line up again.

## Sample Input 0

```
8 12
```

## Sample Output 0

```
24
```

## Sample Input 1

```
5 7
```

## Sample Output 1

```
35
```

## Explanation 0

The announcement plays at minutes `0, 8, 16, 24, 32...`. The jingle plays
at `0, 12, 24, 36...`. The first minute (after 0) where both line up is
**24**.

## Explanation 1

Since `5` and `7` share no common factor (they're coprime), the first time
they line up again is simply `5 × 7 = 35` — there's no shortcut before
that.