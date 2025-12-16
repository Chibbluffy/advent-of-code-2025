def isFresh(i, ranges):
    for r in ranges:
        print(r)
        if r[0] <= i <= r[1]:
            return True
    return False


with open("testinput", "r") as f:
    total = 0
    ranges = []
    r = f.readline().strip()
    while r:
        ranges.append(list(map(int, r.split("-"))))
        r = f.readline().strip()
    ranges.sort()
    print(ranges)

    i = int(f.readline().strip())
    while i:
        print(i)
        if isFresh(i, ranges):
            total += int(i)

        i = f.readline().strip()


print(total)
