
grid = []
found = []

with open('input', 'r') as fp:
    for line in fp:
        grid.append(list(line.strip()))

def find_moves(i, j, n):
    moves = []

    # up
    if i-1 >= 0:
        if grid[i-1][j] == str(int(n) + 1):
            moves.append([i-1, j])
    
    # down
    if i+1 < size:
        if grid[i+1][j] == str(int(n) + 1):
            moves.append([i+1, j])

    # left
    if j-1 >= 0:
        if grid[i][j-1] == str(int(n) + 1):
            moves.append([i, j-1])

    # right
    if j+1 < size:
        if grid[i][j+1] == str(int(n) + 1):
            moves.append([i, j+1])

    return moves


def find(i, j, path):
    if grid[i][j] == '9':
        if (i, j) not in found:
            found.append((i, j))

    for move in find_moves(i, j, grid[i][j]):
        y, x = move
        find(y, x, path + grid[i][j])

size = len(grid)
ans = 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == '0':
            found = []
            find(i, j, '')
            ans += len(found)

print("Sol: ", ans)
