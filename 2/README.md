# Day 2

[Puzzle](https://adventofcode.com/2025/day/2)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

I actually misread the prompt for part 1 and unknowingly did part 2 first by accident.
This one was pretty simple though. I just had to change it from checking for all repeating numbers down to checking if the digits were the same if the number was chopped in half directly in the middle.

```python
from functools import reduce

filename = "input"

invalids = []
with open(filename, "r") as f:
    data = f.readline()
    ranges = data.split(",")
    for r in ranges:
        [min, max] = r.split("-")
        for i in range(int(min), int(max) + 1):
            l = len(str(i))
            if l % 2 == 0:
                if str(i)[: l // 2] == str(i)[l // 2 :]:
                    invalids.append(i)

print(reduce(lambda x, y: x + y, invalids))
```

## Part 2 Work

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.

Here's the solution I had initially. It checks for if the entire number is made up of only a repeating sequence of digits.

```python
from functools import reduce

filename = "input"

invalids = []
with open(filename, "r") as f:
    data = f.readline()
    ranges = data.split(",")
    for r in ranges:
        [min, max] = r.split("-")
        for i in range(int(min), int(max) + 1):
            l = len(str(i))
            for j in range(len(str(i)) // 2 + 1):
                if str(i).replace(str(i)[0:j], "") == "":
                    invalids.append(i)

print(reduce(lambda x, y: x + y, set(invalids)))
```

##### Part 1 puzzle answer 

Your puzzle answer was 19605500130.

##### Part 2 puzzle answer 

Your puzzle answer was 36862281418.
