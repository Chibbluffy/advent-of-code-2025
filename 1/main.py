with open("input", "r") as f:
    zero_count = 0
    curr = 50

    for l in f:
        if l[0].lower() == "l":
            curr -= int(l[1:])
        elif l[0].lower() == "r":
            curr += int(l[1:])
        while curr > 99 or curr < 0:
            if curr > 99:
                curr -= 100
            elif curr < 0:
                curr += 100
        if curr == 0:
            zero_count += 1

print(zero_count)
