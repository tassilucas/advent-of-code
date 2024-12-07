
guard_map = []

with open('input', 'r') as fp:
    for line in fp:
        guard_map.append(list(line.strip()))

def setup():
    for i in range(0, len(guard_map)):
        for j in range(0, len(guard_map)):
            if guard_map[i][j] == '^':
                return [i, j]

def output():
    ans = []
    for step in steps:
        if step not in ans:
            ans.append(step)

    print(len(ans)+1)
    exit()

# after collision, turn 90 degrees to right.
# if function throws exception, means that the next move
# is an outside map move
def collide(i, j):
    try:
        if i-1 < 0 or j-1 < 0:
            raise Exception('Out of bounds')
        elif guard_direction == '^' and guard_map[i-1][j] == '#':
            return '>'
        elif guard_direction == '>' and guard_map[i][j+1] == '#':
            return 'v'
        elif guard_direction == '<' and guard_map[i][j-1] == '#':
            return '^'
        elif guard_direction == 'v' and guard_map[i+1][j] == '#':
            return '<'
        else:
            return None
    except:
        output()
        exit()

def move():
    if guard_direction == '^':
        guard_position[0] -= 1
    elif guard_direction == '>':
        guard_position[1] += 1
    elif guard_direction == 'v':
        guard_position[0] += 1
    elif guard_direction == '<':
        guard_position[1] -= 1

def game():
    inside = True

    while True:
        i, j = guard_position
        collision = collide(i, j)

        if collision is not None:
            global guard_direction
            guard_direction = collision

        move()
        steps.append([i, j])

guard_direction = '^'
guard_position = setup()
steps = []
setup()
game()
