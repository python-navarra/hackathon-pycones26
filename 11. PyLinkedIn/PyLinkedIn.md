It all starts on Friday, in the workshops. That's the first contact, the
icebreaker before the real thing kicks off: someone recognizes another
person by their Mastodon avatar, two strangers discover they've been
hanging out in the same Discord channel for months without knowing it, and
in the coffee line someone asks "wait, are you the one whose PR fixed my
bug on Friday?" — and just like that, a friendship is born for life (or at
least for the whole weekend).

Saturday brings the official opening, the keynotes, the main talks — and
with them, way more people. It doesn't stop. During every lunch break,
every Q&A session, the official speakers' dinner, people keep meeting each
other.

And now, with the conference wrapped up on Sunday night, the organizing
staff wants to close out their stats with an idea they think is brilliant:

—"Let's build something like LinkedIn, but better. For anyone we're
curious about, let's report how many connections are in their networking
web, counting the **entire conference** from start to finish."

Someone raises their hand:

—"Okay, but... like actual LinkedIn? Does it only count people you talked
to directly?"

—"No, no, no," the organizer replies, already wearing that look of someone
who had a brilliant idea at 3 AM. —"Here we apply **Py-transitivity**: if A
knows B, and B knows C, then A and C also count as part of the same
network, even if they've never crossed paths in their lives. It's
mathematically elegant, and it makes the networks grow faster too, which
looks better in the closing stats!"

You get handed the complete list of who met whom over the three days, and a
list of names they want the network size for. All at once, with the
conference already over.

## Problem Statement

There are `n` people at PyConES26, each identified by their **name**. You
are given the complete list of `m` introductions that happened over the
three days: each one states that two people met (and, by Py-transitivity,
their networks — along with everyone already in them — merge into a single
network).

**Note:** the same pair may appear more than once in the list of
introductions (for example, if they crossed paths several times during the
conference). If they were already in the same network, that repeated
introduction simply changes nothing.

After processing **all** the introductions, you are asked `q` questions.
Each question gives the name of a person, and you must answer with the size
of their final network (how many people are in their group, including
themselves). If a person never appeared in any introduction, their network
is still just themselves, size 1.

## Input Format

- The first line contains an integer `n`: the number of people.
- The second line contains `n` names separated by spaces: everyone at
  PyConES26.
- The next line contains an integer `m`: the number of introductions.
- Each of the following `m` lines contains two names `a b` (both guaranteed
  to be present, `a ≠ b`), indicating that those two people met at some
  point during the conference. The same pair may repeat.
- The next line contains an integer `q`: the number of questions.
- Each of the following `q` lines contains a name (guaranteed to be
  present), asking for the size of their final network.

## Constraints

```
1 ≤ n ≤ 2×10^5
0 ≤ m ≤ 2×10^5
1 ≤ q ≤ 2×10^5
Each name has between 1 and 20 characters (letters and digits only, no spaces)
```

## Output Format

Print `q` lines: for each question, a single integer with the final network
size of that person.

## Sample Input 0

```
7
ana bruno carla diego elena fran gonzalo
5
ana bruno
carla diego
bruno carla
elena fran
ana bruno
6
carla
diego
ana
fran
bruno
gonzalo
```

## Sample Output 0

```
4
4
4
2
4
1
```

## Explanation 0

The introduction `ana bruno` appears twice — the second time they were
already in the same network, so nothing changes. After processing all
introductions, three networks remain: `{ana, bruno, carla, diego}` (size
4), `{elena, fran}` (size 2), and `{gonzalo}` alone, having never appeared
in any introduction (size 1). That's why `gonzalo` answers **1**: he never
met anyone, so his network is still just himself.
