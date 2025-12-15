filename = "input"
zero_count = 0
with open(filename, "r") as f:
    curr = 50
    for l in f:
        op = 0
        if l[0].lower() == "l":
            op = 0 - int(l[1:])
        elif l[0].lower() == "r":
            op = int(l[1:])

        while op != 0:
            if op > 0:
                curr += 1
                op -= 1
            elif op < 0:
                curr -= 1
                op += 1
            if curr == 0 or curr == 100:
                zero_count += 1
            if curr == -1:
                curr = 99
            if curr == 100:
                curr = 0

print(zero_count)
