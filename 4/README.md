# Day 4

## --- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

The forklifts can only access a roll of paper if there are *fewer than four rolls of paper* in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are `13` rolls of paper that can be accessed by a forklift (marked with `x`):

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

Consider your complete diagram of the paper roll locations. *How many rolls of paper can be accessed by a forklift?*

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

## --- Part Two ---

Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be *removed*. Once a roll of paper is removed, the forklifts might be able to access *more* rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using `a` to indicate that a roll of paper is about to be removed, and using `x` to indicate that a roll of paper was just removed:

Initial state:
```
..aa.aa@a.
a@@.@.@.@@
@@@@@.a.@@
@.@@@@..@.
a@.@@@@.@a
.@@@@@@@.@
.@.@.@.@@@
a.@@@.@@@@
.@@@@@@@@.
a.a.@@@.a.
```

Remove 13 rolls of paper:
```
..xx.xxax.
x@@.a.a.@a
a@@@@.x.@@
a.@@@@..a.
x@.@@@@.ax
.a@@@@@@.a
.a.@.@.@@@
x.@@@.@@@@
.a@@@@@@@.
x.x.@@@.x.
```

Remove 12 rolls of paper:
```
.......x..
.a@.x.x.ax
x@@@@...aa
x.@@@@..x.
.a.@@@@.x.
.x@@@@@@.x
.x.@.@.@@a
..@@@.@@@@
.xa@@@@@@.
....@@@...
```

Remove 7 rolls of paper:
```
..........
.xa.....x.
.a@@@...xx
..@@@@....
.x.@@@@...
..a@@@@@..
...@.@.@@x
..a@@.@@@a
..x@@@@@@.
....@@@...
```

Remove 5 rolls of paper:
```
..........
..x.......
.xa@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@a.
....@@@...
```

Remove 2 rolls of paper:
```
..........
..........
..x@@.....
..a@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...
```

Remove 1 roll of paper:
```
..........
..........
...a@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

Remove 1 roll of paper:
```
..........
..........
...xa.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

Remove 1 roll of paper:
```
..........
..........
....x.....
...a@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

Remove 1 roll of paper:
```
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of `43` rolls of paper can be removed.

Start with your original diagram. *How many rolls of paper in total can be removed by the Elves and their forklifts?*

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
