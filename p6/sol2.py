
import copy

guard_map = []
ans = 0
d = set()

with open('input', 'r') as fp:
    for line in fp:
        guard_map.append(list(line.strip()))

def setup():
    for i in range(0, len(guard_map)):
        for j in range(0, len(guard_map)):
            if guard_map[i][j] == '^':
                return [i, j]

def collide(i, j, guard_direction, guard_map):
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
        elif guard_direction == '^' and guard_map[i-1][j] == 'O':
            return '>'
        elif guard_direction == '>' and guard_map[i][j+1] == 'O':
            return 'v'
        elif guard_direction == '<' and guard_map[i][j-1] == 'O':
            return '^'
        elif guard_direction == 'v' and guard_map[i+1][j] == 'O':
            return '<'
        else:
            return None
    except:
        return 'END'

def move(guard_direction, guard_position):
    if guard_direction == '^':
        guard_position[0] -= 1
    elif guard_direction == '>':
        guard_position[1] += 1
    elif guard_direction == 'v':
        guard_position[0] += 1
    elif guard_direction == '<':
        guard_position[1] -= 1

def start_game(guard_direction, guard_position, guard_map):
    global ans, d
    d = set()

    while True:
        i, j = guard_position

        if (guard_direction, i, j) in d:
            print("Found")
            ans += 1
            return

        d.add((guard_direction, i, j))
        collision = collide(i, j, guard_direction, guard_map)

        if collision is not None:
            if collision == 'END':
                return
            guard_direction = collision

        move(guard_direction, guard_position)
        steps.append([i, j])

def game():
    inside = True

    for i in range(0, len(default_map)):
        for j in range(0, len(default_map[0])):
            guard_map = copy.deepcopy(default_map)
            guard_position = copy.deepcopy(guard_starter)
            guard_direction = '^'

            if not (i == guard_starter[0] and j == guard_starter[1]) and guard_map[i][j] != '#':
                print(i, j)
                guard_map[i][j] = 'O'
                start_game(guard_direction, guard_position, guard_map)

default_map = copy.deepcopy(guard_map)
guard_direction = '^'
guard_starter = setup()
guard_position = copy.deepcopy(guard_starter)
steps = []
game()
print(ans)
