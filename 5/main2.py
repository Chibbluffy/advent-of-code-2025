def countFresh(ranges):
    total = 0
    for r in ranges:
        total += r[1] - r[0] + 1
    return total

def sortAndMergeRanges(ranges):
    ranges.sort()
    merged_ranges = []
    curr_range = ranges[0]
    for i in range(len(ranges) - 1):
        if ranges[i][1] >= ranges[i+1][0]:
            curr_range[1] = max(curr_range[1], ranges[i+1][1])
        else:
            merged_ranges.append(curr_range)
            curr_range = ranges[i+1]
    merged_ranges.append(curr_range)
    return merged_ranges

with open("input", "r") as f:
    fresh_count = 0
    ranges = []
    r = f.readline().strip()
    while r:
        ranges.append(list(map(int, r.split("-"))))
        r = f.readline().strip()

    ranges = sortAndMergeRanges(ranges)

    print(countFresh(ranges))
