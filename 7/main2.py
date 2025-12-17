def printGrid(grid):
    for g in grid:
        print(''.join(str(g)))


with open("input", "r") as f:
    grid = []
    line = f.readline().strip()
    start = line.find("S")

    while line:
        row = []
        for x in line:
            row.append(x)
        grid.append(row)
        line = f.readline().strip()


grid[1][start] = '1'

for depth in range(1, len(grid)-1):
    if '^' in grid[depth]:
        for i in range(len(grid[depth])):
            # Update path counts for splitters
            if grid[depth][i] == '^' and grid[depth-1][i] not in '.':
                left_index = i - 1
                right_index = i + 1
                # Update left path count
                if grid[depth+1][left_index] == '.':
                    grid[depth+1][left_index] = grid[depth-1][i]
                else:
                    grid[depth+1][left_index] = str(
                        int(grid[depth-1][i]) + int(grid[depth+1][left_index])
                        )
                # Update right path count
                if grid[depth][right_index] == '.':
                    grid[depth+1][right_index] = grid[depth-1][i]
                else:
                    grid[depth][right_index] = str(
                        int(grid[depth-1][i]) + int(grid[depth+1][right_index])
                        )

        # Update path counts for straight paths
        for i in range(len(grid[depth])):
            if grid[depth-1][i] not in '.':
                if grid[depth][i] != '^':
                    if grid[depth+1][i] == '.':
                        grid[depth+1][i] = grid[depth-1][i]
                    else:
                        grid[depth+1][i] = str(
                            int(grid[depth-1][i]) + int(grid[depth+1][i])
                            )

# Sum up total paths at the bottom row
total = 0
for val in grid[-1]:
    if val not in '.':
        total += int(val)
print(total)