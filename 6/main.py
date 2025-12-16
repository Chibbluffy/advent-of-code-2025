import re

with open("input", 'r') as f:
    data = list(map(str.strip, f.read().strip().splitlines()))

    total = 0

    worksheet = []
    for line in data[:-1]:
        l = re.split(r" {1,}", line)
        worksheet.append(list(map(int, l)))
    l = re.split(r" {1,}", data[-1])
    worksheet.append(l)

    for col in range(len(worksheet[0])):
        curr_result = 0 if worksheet[-1][col] == '+' else 1
        for row in range(len(worksheet)-1):
            if worksheet[-1][col] == '+':
                curr_result += worksheet[row][col]

            elif worksheet[-1][col] == '*':
                curr_result *= worksheet[row][col]

        total += curr_result

    print(total)