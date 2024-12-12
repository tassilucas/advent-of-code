
m = []
ans = 0

with open('input', 'r') as fp:
    for line in fp:
        m.append(list(line.strip()))

def calculate_antinodes(h, e, i, j, times):
    d_x = (e - j) * times
    d_y = (h - i) * times

    x = y = w = z = -1

    if d_x < 0:
        x = e - abs(d_x)
        w = j + abs(d_x)
    else:
        x = e + abs(d_x)
        w = j - abs(d_x)

    if d_y < 0:
        y = h - abs(d_y)
        z = i + abs(d_y)
    else:
        y = h + abs(d_y)
        z = i - abs(d_y)

    return (y, x, z, w)

def check_bounds(i, j):
    if (i >= 0 and i < len(m)) and (j >= 0 and j < len(m)):
        return True
    else:
        return False

proc = []

for h in range(len(m[0])):
    for e in range(len(m)):
        if m[h][e] != '.' and m[h][e] != '#':
            for i in range(len(m[0])):
                for j in range(len(m)):
                    if m[i][j] == m[h][e] and i != h and j != e and (h, e, i, j) not in proc:
                        cut1 = cut2 = True
                        times = 1
                        proc.append((h, e, i, j))
                        while cut1 and cut1:
                            y, x, z, w = calculate_antinodes(h, e, i, j, times)
                            if check_bounds(y, x) and cut1:
                                if m[y][x] == '.':
                                    m[y][x] = '#'
                            else:
                                cut1 = False

                            if check_bounds(z, w) and cut2:
                                if m[z][w] == '.':
                                    m[z][w] = '#'
                            else:
                                cut2 = False

                            times += 1

print("Sol: ", sum([len(l) - l.count('.') for l in m]))