# Day 3

[Puzzle](https://adventofcode.com/2025/day/3)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

This was pretty simple. Basically check all the digits except the last digit to find the max, and then check the remaining digits to the right of the first max for a second max. 

```python
filename = "input"
with open(filename, "r") as f:
    l = f.readline().strip()
    total = 0
    while l:
        a = max(map(int, l[:-1]))
        b = max(map(int, l[1 + l.find(str(a)) :]))
        total += int(str(a) + str(b))
        l = f.readline().strip()
print(total)
```

## Part 2 Work

Battery banks must find the largest number made up of 12 digits instead of 2 digits.

This was a simple modification of the first solution. Instead of all except the last digit, it was all except the last 11 digits. The rest of the logic is the same, but repeated instead of only run once.

```python
filename = "input"

def helper(bank, digit):
    if digit != 1:
        a = max(map(int, bank[: 1 - digit]))
        b = helper(bank[1 + bank.find(str(a)) :], digit - 1)
        return int(str(a) + str(b))
    else:
        return max(map(int, bank))

with open(filename, "r") as f:
    l = f.readline().strip()
    total = 0
    while l:
        digits = helper(l, 12)
        total += digits
        l = f.readline().strip()
print(total)
```

##### Part 1 puzzle answer 

Your puzzle answer was 17107.

##### Part 2 puzzle answer 

Your puzzle answer was 169349762274117.
