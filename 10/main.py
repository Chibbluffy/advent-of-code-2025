def extractElements(line):
    temp = line.split("]")
    config = temp[0][1:]
    converted_config = [-1 if c == "." else 1 for c in config]

    temp = temp[1].split("{")
    buttons = temp[0].strip().split(" ")
    converted_buttons = []
    for button in buttons:
        b = list(map(int, button[1:-1].split(",")))
        converted_buttons.append(b)

    joltage = list(map(int, temp[1][:-1].split(",")))

    return converted_config, converted_buttons, joltage


def buttonPressesToConfigure(config, buttons, current_configs):
    presses = 0
    while 1:
        presses += 1
        new_configs = []
        for cc in current_configs:
            for button in buttons:
                temp = cc.copy()
                for index in button:
                    temp[index] *= -1
                if temp == config:
                    return presses
                new_configs.append(temp)
        current_configs = new_configs


with open("input", "r") as f:
    lines = list(map(str.strip, f.read().strip().splitlines()))
    configs = []
    total_button_presses = 0
    for line in lines:
        config, buttons, joltage = extractElements(line)
        base_config = []
        for i in range(len(config)):
            base_config.append(-1)
        total_button_presses += buttonPressesToConfigure(config, buttons, [base_config])

    print(total_button_presses)
