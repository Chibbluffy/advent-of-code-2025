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
