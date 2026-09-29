PyConES 2026 runs on coffee. Lots of coffee.
 
Right next to the main hall, the organisers set up **PyCafé**, a tiny stand with one very tired barista and one very loud espresso machine. Every time someone orders a coffee, the barista writes their name on a list. No names on cups, no loyalty cards, just a list that keeps growing all weekend.
 
On Sunday night, someone from the organising team has a brilliant idea:
 
> *"Let's give a prize to the person who drank the most coffee!"*
 
The barista slides the list across the counter. It has **thousands** of lines, and the same names show up again and again.
 
> *"Counting them by hand would take longer than the conference itself."*
 
You already know who they are going to ask. The editor is open. The espresso machine is still screaming.
 
## Problem Statement
 
You are given the list of names written by the barista, one name per coffee ordered.
 
Find the person who ordered the **most coffees** and print their name and how many coffees they had.
 
If several people are tied for the most coffees, print the one whose name comes **first in alphabetical order**.
 
Names are compared as plain text, so `dev10` comes before `dev2`.
 
## Input Format
 
The first line contains an integer `n`, the number of coffees ordered.
 
Each of the next `n` lines contains one name.
 
## Constraints
 
- `1 ≤ n ≤ 100,000`
- Each name has between `1` and `20` characters.
- Names contain only lowercase English letters and digits.
## Output Format
 
A single line with the winner's name and their number of coffees, separated by a space.
 
## Sample Input 0
 
```
8
lucia
marco
lucia
ana
marco
lucia
ana
marco
```
 
## Sample Output 0
 
```
lucia 3
```
 
## Explanation 0
 
`lucia` and `marco` each ordered 3 coffees and `ana` ordered 2. Since `lucia` and `marco` are tied, the winner is `lucia`, because it comes first alphabetically.