def find_nextempty(puzzle):
    # Finds next empty space, rep= -1
    # Returns row,col or none (if there is none)
    # Using 0-8 indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # If non spaces found

def is_valid(puzzle, guess, row, col):
    # Checks wheather the guess is valid
    # Returns true if valid else false

    # Row check
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Col Check
    # col_vals = []
    # for i in range(9):
    #    col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Find the start of 3x3 grid square starts
    # Then iterate over the 3 values in row/col
    row_start = (row // 3)*3
    col_start = (row // 3)*3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    # If we get here, the checks are valid
    return True

def solve_sudoku(puzzle):
    # Step 1: Choose a location to make a guess
    row, col = find_nextempty(puzzle)
    # If no space left - Done
    if row is None:
        return True
    # Step 2: If space is found, make a guess
    for guess in range(1, 10):
        # Step 3: Check for valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3: If guess is valid, place it in the puzzle
            new_func(puzzle, row, col, guess)
            # Step 4: Recusicvely call the function
            if solve_sudoku(puzzle):
                return True

        # Step 5: If not valid or the guess is wrong
        # Needs to be backtracked
        puzzle[row][col] = -1  # Reset the guess

    # Step 6: If none of the guesses work. The sudoku can not be Solved!
    return False

def new_func(puzzle, row, col, guess):
    puzzle[row][col] == guess