# Day 9

[Puzzle](https://adventofcode.com/2025/day/9)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

This one was actually surprisingly simple compared to the last problem. I also saw on reddit a meme about how Days 9 and 10 were a nightmare. But it's literally just calculating areas. 
You do have to keep in mind that you have to add 1 to each width/height calculation because it is inclusive when doing number lengths like this. 

```python
with open("input", "r") as f:
    lines = list(map(str.strip, f.read().strip().splitlines()))
    tiles = [tuple(map(int, list(x))) for x in [x.split(",") for x in lines]]

    largest_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (
                abs(tiles[i][1] - tiles[j][1]) + 1
            )
            if area > largest_area:
                largest_area = area

    print(largest_area)
```

## Part 2 Work

Part 2 does make this more difficult, but not nightmarishly so. 
Looking at the problem and the given inputs, you can notice something:

```
1: (7, 1)
2: (11, 1)
3: (11, 7)
4: (9, 7)
5: (9, 5)
6: (2, 5)
7: (2, 3)
8: (7, 3)

..............
.......1---2..
.......-----..
..7----8----..
..----------..
..6------5--..
.........---..
.........4-3..
..............

```

When going for any rectangles with nongreen tiles, like 1-3, there are points 4, 5, 8 that are within the area (or in this case, the edge) of the rectangle. So we just have to check for each rectangle, that if it is valid, it must not have any of the other points go inside the area. Or if it is a point touching it, make sure that the next point is going outside, rather than inside or through the rectangle. 

I wrapped the input points by adding the first two tiles to the end of the tiles array. 

```python

```


##### Part 1 puzzle answer 

Your puzzle answer was 4755429952.

##### Part 2 puzzle answer 

Your puzzle answer was .
