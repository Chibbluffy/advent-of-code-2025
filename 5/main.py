def isFresh(i, ranges):
    for r in ranges:
        if r[0] <= i <= r[1]:
            return True
    return False


with open("input", "r") as f:
    fresh_count = 0
    ranges = []
    r = f.readline().strip()
    while r:
        ranges.append(list(map(int, r.split("-"))))
        r = f.readline().strip()
    ranges.sort()

    i = f.readline().strip()
    while i:
        i = int(i)
        if isFresh(i, ranges):
            fresh_count += 1

        i = f.readline().strip()


print(fresh_count)
