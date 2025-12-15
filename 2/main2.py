from functools import reduce

filename = "input"

invalids = []
with open(filename, "r") as f:
    data = f.readline()
    ranges = data.split(",")
    for r in ranges:
        [min, max] = r.split("-")
        for i in range(int(min), int(max) + 1):
            l = len(str(i))
            for j in range(len(str(i)) // 2 + 1):
                if str(i).replace(str(i)[0:j], "") == "":
                    invalids.append(i)

print(reduce(lambda x, y: x + y, set(invalids)))
