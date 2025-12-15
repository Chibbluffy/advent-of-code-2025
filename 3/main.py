filename = "input"
with open(filename, "r") as f:
    l = f.readline().strip()
    total = 0
    while l:
        a = max(map(int, l[:-1]))
        b = max(map(int, l[1 + l.find(str(a)) :]))
        total += int(str(a) + str(b))
        l = f.readline().strip()
print(total)
