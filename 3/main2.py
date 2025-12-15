filename = "input"


def helper(bank, digit):
    if digit != 1:
        a = max(map(int, bank[: 1 - digit]))
        b = helper(bank[1 + bank.find(str(a)) :], digit - 1)
        return int(str(a) + str(b))
    else:
        return max(map(int, bank))


with open(filename, "r") as f:
    l = f.readline().strip()
    total = 0
    while l:
        digits = helper(l, 12)
        total += digits
        l = f.readline().strip()
print(total)
