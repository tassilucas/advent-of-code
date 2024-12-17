
s = []
blinks = 25

with open('input', 'r') as fp:
    s = fp.read().strip().split(' ')

for b in range(blinks):
    line = []
    for stone in s:
        # rule 1
        if stone == '0':
            line.append('1')
        # rule 2
        elif len(stone) % 2 == 0:
            fst = stone[:len(stone) // 2]
            snd = stone[len(stone) // 2:]
            line.append(str(int(fst)))
            line.append(str(int(snd)))
        # rule 3
        else:
            line.append(str(int(stone) * 2024))

    s = line

print("Sol: ", len(s))
