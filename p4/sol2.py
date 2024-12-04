
ipt = []

with open('input', 'r') as fp:
    for line in fp:
        ipt.append(list(line.strip()))

def check_x(i, j, signal):
    word = ''
    try:
        word = ipt[i][j] + ipt[i+(1*signal)][j+1] + ipt[i+(2*signal)][j+2]
    except:
        pass

    return word == 'MAS' or word == 'SAM'

# we only need two diagonals to check this,
# can be d2 and d4
def check_xmas():
    cols = len(ipt[0])
    rows = len(ipt)
    x_mas = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if check_x(i, j, 1) and check_x(i+2, j, -1):
                x_mas += 1

    return x_mas

print(check_xmas())
