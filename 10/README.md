# Day 10

[Puzzle](https://adventofcode.com/2025/day/10)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

I feel like I brute forced this one. Not sure if there is a better way to do it, but there probably definitely is.

```python
def extractElements(line):
    temp = line.split("]")
    config = temp[0][1:]
    converted_config = [-1 if c == "." else 1 for c in config]

    temp = temp[1].split("{")
    buttons = temp[0].strip().split(" ")
    converted_buttons = []
    for button in buttons:
        b = list(map(int, button[1:-1].split(",")))
        converted_buttons.append(b)

    joltage = list(map(int, temp[1][:-1].split(",")))

    return converted_config, converted_buttons, joltage


def buttonPressesToConfigure(config, buttons, current_configs):
    presses = 0
    while 1:
        presses += 1
        new_configs = []
        for cc in current_configs:
            for button in buttons:
                temp = cc.copy()
                for index in button:
                    temp[index] *= -1
                if temp == config:
                    return presses
                new_configs.append(temp)
        current_configs = new_configs


with open("input", "r") as f:
    lines = list(map(str.strip, f.read().strip().splitlines()))
    configs = []
    total_button_presses = 0
    for line in lines:
        config, buttons, joltage = extractElements(line)
        base_config = []
        for i in range(len(config)):
            base_config.append(-1)
        total_button_presses += buttonPressesToConfigure(config, buttons, [base_config])

    print(total_button_presses)

```

## Part 2 Work

I initially set up another recursive solution for this because I thought that the input was nice enough, but on the second line in the input it hung forever, so I knew it would not be a good solution either.

I'll be honest, I got pretty stuck on this one, and decided to look to see how others went about it.
I did not like how most solutions used Z3 or gaussian elimination. Z3 felt like cheating, it made it too easy, and Gaussian elimination felt too high level. Plus, using these required a third party library, which I did not want to do. 

Then I stumbled upon this reddit post:
[Reference](https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/)

It was a bit hard to follow, so I had to read if a few times and ask AI to simplify it. But basically, it's a memoized lookup table combined with a logarithmic scaling.

A simplified explanation, 
WIP

```python

```


##### Part 1 puzzle answer 

Your puzzle answer was 4755429952.

##### Part 2 puzzle answer 

Your puzzle answer was 22517595.
