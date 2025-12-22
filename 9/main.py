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
