# Day 6

[Puzzle](https://adventofcode.com/2025/day/6)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

Math! Instead of performing operations from left to right, it is up and down. After a little parsing magic, it is pretty easy to go through by columns to calculate the result. 

```python
import re

with open("input", 'r') as f:
    data = list(map(str.strip, f.read().strip().splitlines()))

    total = 0

    worksheet = []
    for line in data[:-1]:
        l = re.split(r" {1,}", line)
        worksheet.append(list(map(int, l)))
    l = re.split(r" {1,}", data[-1])
    worksheet.append(l)

    for col in range(len(worksheet[0])):
        curr_result = 0 if worksheet[-1][col] == '+' else 1
        for row in range(len(worksheet)-1):
            if worksheet[-1][col] == '+':
                curr_result += worksheet[row][col]

            elif worksheet[-1][col] == '*':
                curr_result *= worksheet[row][col]

        total += curr_result

    print(total)
```

## Part 2 Work

We have been under the wrong impression for the math. It is not the full number left to right, it is up to down. 

We have to change our parsing to grab the numbers correctly, but the rest of it is the same logic. 

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

Your puzzle answer was 3525371263915.

##### Part 2 puzzle answer 

Your puzzle answer was 6846480843636.
