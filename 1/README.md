# Day 1

[Puzzle](https://adventofcode.com/2025/day/1)
[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)
[Part 2 puzzle answer](#part-2-puzzle-answer)
  
  
## Part 1 Work

This is an attempt at efficiently counting the zero's it stops on. It works fine.
It can be improved by dividing by 100 instead of incrementing/decrementing.
```python

with open("input", "r") as f:
    zero_count = 0
    curr = 50

    for l in f:
        if l[0].lower() == "l":
            curr -= int(l[1:])
        elif l[0].lower() == "r":
            curr += int(l[1:])
        while curr > 99 or curr < 0:
            if curr > 99:
                curr -= 100
            elif curr < 0:
                curr += 100
        if curr == 0:
            zero_count += 1

print(zero_count)
```
  
## Part 2 Work

For part 2, instead of counting only the 0's it stops on, it needs to count every time 0 is clicked on or clicked past.

I couldn't figure out a good formula or simplified logic that could capture all the zero's that are passed on by the lock, so I defaulted to the basic brute force method. 

```python
filename = "input"
zero_count = 0
with open(filename, "r") as f:
    curr = 50
    for l in f:
        op = 0
        if l[0].lower() == "l":
            op = 0 - int(l[1:])
        elif l[0].lower() == "r":
            op = int(l[1:])

        while op != 0:
            if op > 0:
                curr += 1
                op -= 1
            elif op < 0:
                curr -= 1
                op += 1
            if curr == 0 or curr == 100:
                zero_count += 1
            if curr == -1:
                curr = 99
            if curr == 100:
                curr = 0

print(zero_count)
```


##### Part 1 puzzle answer 

The puzzle answer was 1182.

##### Part 2 puzzle answer

The puzzle answer was 6907.
