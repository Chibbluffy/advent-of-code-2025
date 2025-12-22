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


def pressButton(button, joltage):
    for b in button:
        joltage[b] -= 1
    return joltage


def filterButtons(joltage, buttons):
    valid_buttons = []
    for button in buttons:
        valid_button = True
        for b in button:
            if joltage[b] == 0:
                valid_button = False
        if valid_button:
            valid_buttons.append(button)
    return valid_buttons


def joltageStatus(joltage):
    under = False
    nonzeros = 0
    for j in joltage:
        if j < 0:
            under = True
        elif j != 0:
            nonzeros += 1
    if under:
        return -1
    elif nonzeros:
        return 1
    return 0


def buttonPressesToConfigureHelper(joltage, buttons, presses):
    if joltageStatus(joltage) == 0:
        return presses

    valid_buttons = filterButtons(joltage, buttons)

    for i, button in enumerate(valid_buttons):
        temp_voltage = pressButton(button, joltage.copy())
        result = buttonPressesToConfigureHelper(
            temp_voltage, valid_buttons[i:], presses + 1
        )
        if result is not None:
            return result
    return None


import numpy as np


def solve_with_matrix(joltage, buttons):
    # 1. Create the Matrix A
    # Rows = joltage positions, Columns = buttons
    num_positions = len(joltage)
    num_buttons = len(buttons)

    A = np.zeros((num_positions, num_buttons))

    for col, button in enumerate(buttons):
        for position in button:
            A[position, col] = 1

    # 2. Create Vector B
    B = np.array(joltage)

    # 3. Solve for X
    # Since the matrix might not be square, we use least squares
    # or pinv (pseudo-inverse) to find the exact integer solution
    try:
        x, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)

        # 4. Clean up the results
        # Pressing a button must be an integer count
        x = np.round(x).astype(int)

        # Verify the solution
        if np.all(np.dot(A, x) == B):
            return sum(x)
        else:
            return "No exact integer solution found"
    except np.linalg.LinAlgError:
        return "Matrix is singular or unsolvable"


def buttonPressesToConfigure(joltage, buttons):
    valid_buttons = filterButtons(joltage, buttons)
    return solve_with_matrix(joltage, valid_buttons)
    # return buttonPressesToConfigureHelper(joltage, valid_buttons, 0)


with open("input", "r") as f:
    lines = list(map(str.strip, f.read().strip().splitlines()))
    total_button_presses = 0
    for line in lines:
        config, buttons, joltage = extractElements(line)
        print(joltage, buttons)
        # Sort such that buttons which affect more counters are first
        buttons.sort(key=lambda x: len(x), reverse=True)
        empty_joltage = [0 for _ in joltage]
        total_button_presses += buttonPressesToConfigure(joltage, buttons)

    print(total_button_presses)
