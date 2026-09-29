## Story

The organisers of PyConES 2026 decided to launch a challenge for all participants: **the Py-rate Radio**. A small speaker connected to an old laptop, with a floppy disk that holds a random message which changes every hour — programmer jokes, talk schedules, hackathon gossip, places to visit in Barcelona, even rumours about the latest NumPy release.

At first it's a fun little game: small shifts, short messages. People laugh as they decrypt them by hand on a piece of paper while waiting for the next talk.

But once the organisers saw how easily the challenges were being solved — and how much the participants were enjoying it — they decided to raise the difficulty: shifts with **six digits**. Yes, six digits. Suddenly, everyone is asking the same question: *"what does this even say?"*

That's when someone opened PyCharm, and the lines of code started running. Yeah.

## Problem Statement

Write a **Python** program that reads a string and a non-negative integer `k` (the shift), and prints the string after applying a **Caesar cipher** over the **26-letter English alphabet** (`a`-`z` / `A`-`Z`): every letter is shifted `k` positions forward in the alphabet, wrapping around from `z` back to `a` (and from `Z` back to `A`) as many times as needed.

Uppercase letters must remain uppercase, lowercase letters must remain lowercase. Any character that is **not** one of these 26 English letters — digits, spaces, punctuation, accented letters, `ñ`, etc. — must remain unchanged.

## Input Format

```
S
k
```

- Line 1: the string `S` (may contain spaces).
- Line 2: an integer `k`, the shift.

## Constraints

1. `1 ≤ len(S) ≤ 500`
2. `0 ≤ k ≤ 10^6`
3. `S` may contain uppercase/lowercase letters, digits, spaces, and punctuation.
4. Since `k` can be much larger than 26, it must effectively be treated as `k mod 26`.

## Output Format

A single line: the string `S` after applying the Caesar shift.