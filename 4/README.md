# Day 4

[Puzzle](https://adventofcode.com/2025/day/4)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

I read this problem wrong at first as well. I initially thought it was if there were 4 empty cells around a roll, it could be removed. Then I reread it and misread it again again. Second time I thought it said if if was 4 adjacent empty spots. Third time was the charm here, it's if there are 5 or more empty cells around a roll. 

```python
def enoughEmptyAdjacents(surroundings):
    count = 0
    for s in surroundings:
        if s == ".":
            count += 1
        if count >= 5:
            return True

with open("input", "r") as f:
    line = f.readline().strip()
    data = []
    d1 = ["." for x in range(len(line) + 2)]
    data.append(d1)
    while line:
        d = ["."]
        for c in line:
            d.append(c)
        d.append(".")
        data.append(d)
        line = f.readline().strip()
    data.append(d1)

extractable_rolls = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] == "@":
            tl = data[i - 1][j - 1]
            tm = data[i - 1][j]
            tr = data[i - 1][j + 1]
            mr = data[i][j + 1]
            br = data[i + 1][j + 1]
            bm = data[i + 1][j]
            bl = data[i + 1][j - 1]
            ml = data[i][j - 1]
            if enoughEmptyAdjacents([tl, tm, tr, mr, br, bm, bl, ml]):
                data[i][j] = "x"
                extractable_rolls += 1

print(extractable_rolls)
```

## Part 2 Work

Now instead of counting the ones that can be removed, we need to count every roll that is removed, and remove them until no more can be removed to return the total. 

This was pretty simple to adapt to update the grid, and count/remove rolls until there were no more removable rolls. Just wrap it in a while loop, until there are no more removable rolls while keeping count.

```python
def enoughEmptyAdjacents(surroundings):
    count = 0
    for s in surroundings:
        if s == ".":
            count += 1
        if count >= 5:
            return True


with open("input", "r") as f:
    line = f.readline().strip()
    data = []
    d1 = ["." for x in range(len(line) + 2)]
    data.append(d1)
    while line:
        d = ["."]
        for c in line:
            d.append(c)
        d.append(".")
        data.append(d)
        line = f.readline().strip()
    data.append(d1)

extractable_rolls = 0
just_extracted = 1
while just_extracted:
    just_extracted = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] == "@":
                tl = data[i - 1][j - 1]
                tm = data[i - 1][j]
                tr = data[i - 1][j + 1]
                mr = data[i][j + 1]
                br = data[i + 1][j + 1]
                bm = data[i + 1][j]
                bl = data[i + 1][j - 1]
                ml = data[i][j - 1]
                if enoughEmptyAdjacents([tl, tm, tr, mr, br, bm, bl, ml]):
                    data[i][j] = "."
                    just_extracted += 1
                    extractable_rolls += 1

print(extractable_rolls)

```

##### Part 1 puzzle answer 

Your puzzle answer was 1564.

##### Part 2 puzzle answer 

Your puzzle answer was 9401.
