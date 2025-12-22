with open("testinput", "r") as f:
    lines = list(map(str.strip, f.read().strip().splitlines()))
    tiles = [tuple(map(int, list(x))) for x in [x.split(",") for x in lines]]
    tiles.append(tiles[0])
    tiles.append(tiles[1])

    largest_area = 0
    for i in range(len(tiles) - 2):
        for j in range(i + 1, len(tiles) - 2):
            tile_a = tiles[i]
            tile_b = tiles[j]
            # print(f"Processing: ({tile_a}), ({tile_b})")
            area = 0
            valid_area = True
            # Add a check for if any other points are touching or within the rectangle
            x1 = min(tile_a[0], tile_b[0])
            x2 = max(tile_a[0], tile_b[0])
            y1 = min(tile_a[1], tile_b[1])
            y2 = max(tile_a[1], tile_b[1])
            for k in range(1, len(tiles) - 1):
                if k == i or k == j:
                    continue
                # print("Is this tile inside? ", tiles[k])
                # Completely inside
                if x1 < tiles[k][0] < x2 and y1 < tiles[k][1] < y2:
                    # print("no1")
                    valid_area = False
                    break
                # Touching X
                elif (x1 == tiles[k][0] or x2 == tiles[k][0]) and y1 <= tiles[k][
                    1
                ] <= y2:
                    # print("touching on X")
                    if y1 < tiles[k - 1][1] < y2 or y1 < tiles[k + 1][1] < y2:
                        valid_area = False
                        # print("no2")
                        break

                # Touching Y
                elif (y1 == tiles[k][1] or y2 == tiles[k][1]) and x1 <= tiles[k][
                    0
                ] <= x2:
                    # print("touching on Y")
                    if x1 < tiles[k - 1][0] < x2 or x1 < tiles[k + 1][0] < x2:
                        valid_area = False
                        # print("no3")
                        break

            # print(f"Valid: {valid_area}")
            # print((abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1))
            if valid_area:
                area = (abs(tile_a[0] - tile_b[0]) + 1) * (
                    abs(tile_a[1] - tile_b[1]) + 1
                )
            if area > largest_area:
                largest_area = area

    print(largest_area)
