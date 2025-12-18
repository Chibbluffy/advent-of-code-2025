# Day 5

## --- Day 5: Cafeteria ---

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are *fresh* and which are *spoiled*. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on *ingredient IDs*. It consists of a list of *fresh ingredient ID ranges*, a blank line, and a list of *available ingredient IDs*. For example:

```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

The fresh ID ranges are *inclusive*: the range `3-5` means that ingredient IDs `3`, `4`, and `5` are all *fresh*. The ranges can also *overlap*; an ingredient ID is fresh if it is in *any* range.

The Elves are trying to determine which of the *available ingredient IDs* are *fresh*. In this example, this is done as follows:

- Ingredient ID `1` is spoiled because it does not fall into any range.
- Ingredient ID `5` is *fresh* because it falls into range `3-5`.
- Ingredient ID `8` is spoiled.
- Ingredient ID `11` is *fresh* because it falls into range `10-14`.
- Ingredient ID `17` is *fresh* because it falls into range `16-20` as well as range `12-18`.
- Ingredient ID `32` is spoiled.

So, in this example, `3` of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. *How many of the available ingredient IDs are fresh?*

[Part 1 puzzle answer](#part-1-puzzle-answer)

## --- Part Two ---
--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know *all* of the IDs that the *fresh ingredient ID ranges* consider to be *fresh*. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

```
3-5
10-14
16-20
12-18
```

The ingredient IDs that these ranges consider to be fresh are `3`, `4`, `5`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, and `20`. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. *How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?*

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

Just check if each given ingredient id falls in any range. I sorted it just in case.

```python
def isFresh(i, ranges):
    for r in ranges:
        if r[0] <= i <= r[1]:
            return True
    return False

with open("input", "r") as f:
    fresh_count = 0
    ranges = []
    r = f.readline().strip()
    while r:
        ranges.append(list(map(int, r.split("-"))))
        r = f.readline().strip()
    ranges.sort()

    i = f.readline().strip()
    while i:
        i = int(i)
        if isFresh(i, ranges):
            fresh_count += 1

        i = f.readline().strip()

print(fresh_count)

```

## Part 2 Work

The modification for this part is to only take the ranges, and merge the ranges if any of them overlap. Sorting helps tremendously here. I probably should rename countFresh to findTotalRange or something. 

```python
def countFresh(ranges):
    total = 0
    for r in ranges:
        total += r[1] - r[0] + 1
    return total

def sortAndMergeRanges(ranges):
    ranges.sort()
    merged_ranges = []
    curr_range = ranges[0]
    for i in range(len(ranges) - 1):
        if ranges[i][1] >= ranges[i+1][0]:
            curr_range[1] = max(curr_range[1], ranges[i+1][1])
        else:
            merged_ranges.append(curr_range)
            curr_range = ranges[i+1]
    merged_ranges.append(curr_range)
    return merged_ranges

with open("input", "r") as f:
    fresh_count = 0
    ranges = []
    r = f.readline().strip()
    while r:
        ranges.append(list(map(int, r.split("-"))))
        r = f.readline().strip()

    ranges = sortAndMergeRanges(ranges)

    print(countFresh(ranges))
```

##### Part 1 puzzle answer 

Your puzzle answer was 782.

##### Part 2 puzzle answer 

Your puzzle answer was 353863745078671.
