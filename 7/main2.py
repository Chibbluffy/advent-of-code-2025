def flatten(arr):
    newArray = []
    for a in arr:
        if isinstance(a, list):
            newArray.append(a[0])
            newArray.append(a[1])
        else:
            newArray.append(a)
    return list(set(newArray))


with open("input", "r") as f:
    paths = 1
    line = f.readline().strip()
    start = line.find("S")
    beam = [start]
    splits = 0
    line = f.readline().strip()
    while line:
        for i in range(len(beam)):
            if line[beam[i]] == "^":
                splits += 1
                beam[i] = [beam[i] - 1, beam[i] + 1]
        paths += splits
        beam = flatten(beam)
        line = f.readline().strip()
print(splits)
