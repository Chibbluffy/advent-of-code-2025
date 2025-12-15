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
            if l % 2 == 0:
                if str(i)[: l // 2] == str(i)[l // 2 :]:
                    invalids.append(i)

print(reduce(lambda x, y: x + y, invalids))
