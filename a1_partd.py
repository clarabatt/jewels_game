# copy over your a1_partd.py file here
# don't forget to update your overflow() function

#    Main Author(s):
#    Main Reviewer(s):

from a1_partc import Queue


def get_overflow_list(grid):
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

    return 1 + overflow(new_grid, a_queue)
