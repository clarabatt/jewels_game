from queue import Queue


def get_overflow_list(grid):
    """
    Identify the cells that are overflowing
    Return: the list of cells that overflow.
    If no cells meet the criteria, it returns None
    """
    cells = []
    for i, lines in enumerate(grid):
        for j, cell in enumerate(lines):
            counter = 0
            if i - 1 >= 0:
                counter += 1
            if i + 1 < len(grid):
                counter += 1
            if j - 1 >= 0:
                counter += 1
            if j + 1 < len(lines):
                counter += 1
            if abs(cell) >= counter:
                cells.append([i, j])
    if len(cells) == 0:
        return None
    return cells


def overflow(grid, a_queue):
    """
    Modifies the board passed based on the overflow rule and uses recursion to handle subsequent overflows resulting from the initial changes.
    Return: The number of times the overflow rule was applied.
    """
    overflow_list = get_overflow_list(grid)
    if overflow_list is None:
        return 0

    # Deep Copy
    new_grid = [[cell for cell in row] for row in grid]

    print(f"Processing grid: {new_grid}")
    print(f"Overflow list: {overflow_list}")

    for cell in overflow_list:
        i = cell[0]
        j = cell[1]
        if i - 1 >= 0:
            new_grid[i - 1][j] = (new_grid[i][j] / abs(new_grid[i][j])) * (
                abs(new_grid[i - 1][j]) + 1
            )
        if i + 1 < len(grid):
            new_grid[i + 1][j] = (new_grid[i][j] / abs(new_grid[i][j])) * (
                abs(new_grid[i + 1][j]) + 1
            )
        if j - 1 >= 0:
            new_grid[i][j - 1] = (new_grid[i][j] / abs(new_grid[i][j])) * (
                abs(new_grid[i][j - 1]) + 1
            )
        if j + 1 < len(grid[i]):
            new_grid[i][j + 1] = (new_grid[i][j] / abs(new_grid[i][j])) * (
                abs(new_grid[i][j + 1]) + 1
            )

        if new_grid[i][j] > 0:
            new_grid[i][j] = new_grid[i][j] - abs(grid[i][j])
        else:
            new_grid[i][j] = -(abs(new_grid[i][j]) - abs(grid[i][j]))

    a_queue.enqueue(new_grid)

    same_sign = all(
        all(cell >= 0 for cell in row) or all(cell < 0 for cell in row)
        for row in new_grid
    )
    if same_sign:
        return 1

    return 1 + overflow(new_grid, a_queue)
