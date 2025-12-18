# Day 7

[Puzzle](https://adventofcode.com/2025/day/7)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

This puzzle was really cool, I liked it. There are a couple ways to do this.

I could have done recursion the for this one, but I didn't until later.
I kept track of the indices and performed the splits whenever there was a splitter.
To prevent duplicates, I used `set` when I flattened the indices.

```python
def flatten(arr):
    newArray = []
    for a in arr:
        if isinstance(a, list):
            newArray.append(a[0])
            newArray.append(a[1])
        else:
            newArray.append(a)
    return list(set(newArray))


with open("input", "r") as f:
    line = f.readline().strip()
    start = line.find("S")
    beam = [start]
    splits = 0
    line = f.readline().strip()
    while line:
        for i in range(len(beam)):
            if line[beam[i]] == "^":
                splits += 1
                beam[i] = [beam[i] - 1, beam[i] + 1]
        beam = flatten(beam)
        line = f.readline().strip()
print(splits)

```

## Part 2 Work

Now this was tricky. Instead of finding just the splits, it wants to know the total number of paths that can be possible to reach the end. 

Here, I thought recursion would be best. Boy howdy was I wrong. I had to find a better way to work through this problem. I did still use recursion as a tool to figure out my logic and the answers for smaller inputs though. 

Here's the recursion version I used:

```python
# Do NOT use this file on the large input, it's just for helping find the small scale solutions

def path(grid, depth, index):
    if depth == len(grid):
        return 1
    if grid[depth][index] == "^":
        return path(grid, depth + 1, index - 1) + path(grid, depth + 1, index + 1)
    else:
        return path(grid, depth + 1, index)


with open("testinput", "r") as f:
    grid = []
    line = f.readline().strip()
    grid.append(line)
    start = line.find("S")
    while line:
        grid.append(line)
        line = f.readline().strip()
    print(path(grid, 0, start))
```

From this, I was able to try and work through the answer

```
.......S.......
......|^|...... 2
.....|^|^|..... 4
....|^|^|^|.... 8
...|^|^|||^|... 13
..|^|^|||^|^|.. 20
.|^|||^||.||^|. 26
|^|^|^|^|^|||^| 40

.......S....... 1
.......|....... 1
......|^|...... 2 ?= 1 splitter, 2 beams
......|.|...... 2
.....|^|^|..... 4 ?= 2+1=3 splitters, 3 beams
.....|.|.|..... 4
....|^|^|^|.... 8 ?= 3+3=6 splitters, 4 beams
....|.|.|.|.... 8
...|^|^|||^|... 13 ?= 3+6=9 splitters, 6 beams
...|.|.|||.|... 13
..|^|^|||^|^|.. 20 ?= 4+9=13 splitters, 7 beams
..|.|.|||.|.|.. 20
.|^|||^||.||^|. 26 ?= 3+13=16 splitters, 9 beams
.|.|||.||.||.|. 26
|^|^|^|^|^|||^| 40 ?= 6+16=22 splitters, 9 beams
|.|.|.|.|.|||.| 40
```

It took me one night to think through it, but I did figure out a way to calculate the total path count after working it out a few times on scratch paper.

```
       1        1
	  1 1       2
	 1 2 1      4
	1 3 3 1     8
   1 4 331 1    13
  1 5 434 2 1   20
 1 154 74021 1  26
```

I'm not able to digitally create a visually appealing version, but here is an attempt:

```
['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '1', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '^', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '1', '.', '1', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '1', '.', '2', '.', '1', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '^', '.', '^', '.', '^', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '1', '.', '3', '.', '3', '.', '1', '.', '.', '.', '.']
['.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.']
['.', '.', '.', '1', '.', '4', '.', '3', '3', '1', '.', '1', '.', '.', '.']
['.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '^', '.', '.', '.']
['.', '.', '1', '.', '5', '.', '4', '3', '4', '.', '2', '.', '1', '.', '.']
['.', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.', '.', '^', '.', '.']
['.', '1', '.', '1', '5', '4', '.', '7', '4', '.', '2', '1', '.', '1', '.']
['.', '^', '.', '^', '.', '^', '.', '^', '.', '^', '.', '.', '.', '^', '.']
['1', '.', '2', '.', '10', '.', '11', '.', '11', '.', '2', '1', '1', '.', '1']
```

Basically, each splitter will move the number down on both sides. If a number already exists there, add them together. If there is no splitter, move the number down directly. Same as before, if a number already exists in that spot, add them together. 

Then at the very end, add everything together on the last line.

```python
with open("input", "r") as f:
    data = f.read().splitlines()
    total = 0
    nums = []

    for i in range(len(data[0]) - 1, -1, -1):
        num = ""

        # parse numbers
        for j in range(len(data)):
            if data[j][i] != " ":
                num += data[j][i] if data[j][i] != "+" and data[j][i] != "*" else ""

        # clear calculation for next batch
        if num == "":
            nums = []
            continue

        nums.append(int(num))

        if data[-1][i] == "+":
            total += sum(nums)
        elif data[-1][i] == "*":
            prod = 1
            for n in nums:
                prod *= n
            total += prod

    print(total)
```

##### Part 1 puzzle answer 

Your puzzle answer was 1546.

##### Part 2 puzzle answer 

Your puzzle answer was 13883459503480.
