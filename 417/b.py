h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(input().strip())


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(row, col):
    return 0 <= row < h and 0 <= col < w

def count_adjacent_black(row, col):
    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid(new_row, new_col) and grid[new_row][new_col] == '#':
            count += 1
    return count

valid = True
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            adjacent_black = count_adjacent_black(i, j)
            if adjacent_black != 2 and adjacent_black != 4:
                valid = False
                break
    if not valid:
        break

if valid:
    print("Yes")
else:
    print("No")