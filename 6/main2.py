import re

with open("testinput", 'r') as f:
    data = f.read().splitlines()
    total = 0

    for i in range(len(data[0])-1, -1, -1):
        nums = []
        num = ''
        for j in range(len(data)):
            if data[j][i] != ' ':
                num += data[j][i] if data[j][i] != '+' and data[j][i] != '*' else ''
        print(num)
        if num != '':
            nums.append(int(num))
        print(nums)
        if data[-1][i] == '+':
            total += sum(nums)
        elif data[-1][i] == '*':
            prod = 1
            for n in nums:
                prod *= n
            total += prod

    print(total)