# Day 5

[Puzzle](https://adventofcode.com/2025/day/5)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

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

Instead of counting the fresh ingredients on hand, they want to know the total number of fresh ingredients.

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
