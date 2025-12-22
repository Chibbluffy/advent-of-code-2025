def solve_pure_python(joltage, buttons):
    num_vars = len(buttons)
    num_eqs = len(joltage)
    
    # 1. Create Augmented Matrix: [A | B]
    # Rows = joltage positions, Columns = buttons + 1 (for the result)
    matrix = [[0.0] * (num_vars + 1) for _ in range(num_eqs)]
    for col, button in enumerate(buttons):
        for pos in button:
            matrix[pos][col] = 1.0
    for i in range(num_eqs):
        matrix[i][num_vars] = float(joltage[i])

    # 2. Gaussian Elimination (Forward Pass)
    pivot_row = 0
    pivot_cols = []
    for col in range(num_vars):
        if pivot_row >= num_eqs:
            break
            
        # Find best row for pivot
        sel_row = pivot_row
        while sel_row < num_eqs and abs(matrix[sel_row][col]) < 1e-9:
            sel_row += 1
            
        if sel_row == num_eqs:
            continue # No pivot in this column

        # Swap rows
        matrix[pivot_row], matrix[sel_row] = matrix[sel_row], matrix[pivot_row]
        pivot_cols.append(col)

        # Normalize pivot row
        pivot_val = matrix[pivot_row][col]
        matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]

        # Eliminate other rows
        for r in range(num_eqs):
            if r != pivot_row:
                factor = matrix[r][col]
                matrix[r] = [matrix[r][i] - factor * matrix[pivot_row][i] for i in range(num_vars + 1)]
        
        pivot_row += 1

    # 3. Extract Solution
    presses = [0] * num_vars
    for i, col in enumerate(pivot_cols):
        # We round because button presses must be integers
        presses[col] = int(round(matrix[i][num_vars]))

    return sum(presses)

# Test with your data
joltage = [64, 68, 82, 53, 82, 69, 85, 121, 51, 77]
buttons = [[6, 7, 9], [1, 4, 6, 7, 8], [1, 2, 3, 5, 6, 7], [4, 5, 7], [1, 9], [6, 7], [0, 1, 2, 4, 5, 7, 9], [1, 3, 4, 5, 6, 7, 9], [1, 2, 5, 6, 8, 9], [0, 2, 4, 5, 6, 8, 9], [0, 2, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 6, 7, 8], [0, 1, 2, 3, 4, 7, 8, 9]]

print(solve_pure_python(joltage, buttons))