with open("input", "r") as f:
    data = f.read().splitlines()
    total = 0
    nums = []

    for i in range(len(data[0]) - 1, -1, -1):
        num = ""

        # parse numbers
        for j in range(len(data)):
            if data[j][i] != " ":
                num += data[j][i] if data[j][i] != "+" and data[j][i] != "*" else ""

        # clear calculation for next batch
        if num == "":
            nums = []
            continue

        nums.append(int(num))

        if data[-1][i] == "+":
            total += sum(nums)
        elif data[-1][i] == "*":
            prod = 1
            for n in nums:
                prod *= n
            total += prod

    print(total)
