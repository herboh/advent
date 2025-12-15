def count_adjacent_rolls(matrix, row, col, target_value):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] == target_value:
                count += 1

    return count

# just for fun
def count_total_rolls(matrix):
    count = 0
    for row in matrix:
        for cell in row:
            if cell == '@':
                count += 1
    return count

# Solution
def remove_rolls(matrix, iteration=1, num_removed=0):
    rows = len(matrix)
    cols = len(matrix[0])
    removable_rolls = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Only check positions that contain '@'
            if matrix[i][j] == '@':
                adjacent_count = count_adjacent_rolls(matrix, i, j, '@')
                if adjacent_count < 4:
                    removable_rolls.append((i, j))

    if not removable_rolls:
        print(f"\nNo more rolls can be removed")
        print("\n--- Final Matrix ---")
        for row in matrix:
            print("".join(row))
        print("--------------------")
        print(f"Number of wrapping paper rolls removed = {num_removed}")
        print(f"Remaining Rolls = {count_total_rolls(matrix)}")

        return matrix, num_removed

    for r, c in removable_rolls:
        matrix[r][c] = '.'

    num_removed += len(removable_rolls)
    remaining = count_total_rolls(matrix)
    print(f"Generation {iteration}: Removed {len(removable_rolls)} rolls | Total removed: {num_removed} | Remaining '@': {remaining}")
    return remove_rolls(matrix, iteration + 1, num_removed)

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]
    initial_count = count_total_rolls(matrix)
    print(f"Initial Number of Rolls {initial_count}\n")
    matrix, total_removed = remove_rolls(matrix)
