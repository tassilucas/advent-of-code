
ipt = []

with open('input', 'r') as fp:
    for line in fp:
        ipt.append(list(line.strip()))

def check_vertical_up(i, j):
    word = ''
    if i-1 >= 0 and i-2 >= 0 and i-3 >= 0:
        word = ipt[i][j] + ipt[i-1][j] + ipt[i-2][j] + ipt[i-3][j]

    return word == 'XMAS'

def check_vertical_down(i, j):
    word = ''
    try:
        word = ipt[i][j] + ipt[i+1][j] + ipt[i+2][j] + ipt[i+3][j]
    except:
        pass

    return word == 'XMAS'

def check_horizontal_left(i, j):
    word = ''
    if j-1 >= 0 and j-2 >= 0 and j-3 >= 0:
        word = ipt[i][j] + ipt[i][j-1] + ipt[i][j-2] + ipt[i][j-3]

    return word == 'XMAS'

def check_horizontal_right(i, j):
    word = ''
    try:
        word = ipt[i][j] + ipt[i][j+1] + ipt[i][j+2] + ipt[i][j+3]
    except:
        pass

    return word == 'XMAS'

def check_d1(i, j):
    word = ''
    if i-1 >= 0 and i-2 >= 0 and i-3 >= 0 and \
        j-1 >= 0 and j-2 >= 0 and j-3 >= 0:
            word = ipt[i][j] + ipt[i-1][j-1] + ipt[i-2][j-2] + ipt[i-3][j-3]

    return word == 'XMAS'

def check_d2(i, j):
    word = ''
    if i-1 >= 0 and i-2 >= 0 and i-3 >= 0:
        try:
            word = ipt[i][j] + ipt[i-1][j+1] + ipt[i-2][j+2] + ipt[i-3][j+3]
        except:
            pass

    return word == 'XMAS'

def check_d3(i, j):
    word = ''
    if j-1 >= 0 and j-2 >= 0 and j-3 >= 0:
        try:
            word = ipt[i][j] + ipt[i+1][j-1] + ipt[i+2][j-2] + ipt[i+3][j-3]
        except:
            pass

    return word == 'XMAS'

def check_d4(i, j):
    word = ''
    try:
        word = ipt[i][j] + ipt[i+1][j+1] + ipt[i+2][j+2] + ipt[i+3][j+3]
    except:
        pass

    return word == 'XMAS'

# this might be the dumbest solution
def check_xmas():
    cols = len(ipt[0])
    rows = len(ipt)
    xmas = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if ipt[i][j] == 'X':
                if check_vertical_down(i, j):
                    xmas += 1
                if check_vertical_up(i, j):
                    xmas += 1
                if check_horizontal_left(i, j):
                    xmas += 1
                if check_horizontal_right(i, j):
                    xmas += 1
                if check_d1(i, j):
                    xmas += 1
                if check_d2(i, j):
                    xmas += 1
                if check_d3(i, j):
                    xmas += 1
                if check_d4(i, j):
                    xmas += 1

    return xmas

print(check_xmas())
