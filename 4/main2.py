def enoughEmptyAdjacents(surroundings):
    count = 0
    for s in surroundings:
        if s == ".":
            count += 1
        if count >= 5:
            return True


with open("input", "r") as f:
    line = f.readline().strip()
    data = []
    d1 = ["." for x in range(len(line) + 2)]
    data.append(d1)
    while line:
        d = ["."]
        for c in line:
            d.append(c)
        d.append(".")
        data.append(d)
        line = f.readline().strip()
    data.append(d1)


extractable_rolls = 0
just_extracted = 1
while just_extracted:
    just_extracted = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if data[i][j] == "@":
                tl = data[i - 1][j - 1]
                tm = data[i - 1][j]
                tr = data[i - 1][j + 1]
                mr = data[i][j + 1]
                br = data[i + 1][j + 1]
                bm = data[i + 1][j]
                bl = data[i + 1][j - 1]
                ml = data[i][j - 1]
                if enoughEmptyAdjacents([tl, tm, tr, mr, br, bm, bl, ml]):
                    data[i][j] = "."
                    just_extracted += 1
                    extractable_rolls += 1


print(extractable_rolls)
