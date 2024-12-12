
disk_file = None

with open('input', 'r') as fp:
    disk_file = fp.read().strip()

rep = []
id = 0

# transforming to disk file to representation
for idx, c in enumerate(disk_file):
    for i in range(int(c)):
        if idx % 2 == 0:
            rep.append(str(id))
        else:
            rep += '.'

    if idx % 2:
        id += 1

ptr = len(rep) - 1

while True:
    empty = rep.index('.')

    if ptr <= empty:
        break
    elif rep[ptr] == '.' and empty < ptr:
        ptr -= 1
        continue

    rep[empty], rep[ptr] = rep[ptr], rep[empty]
    ptr -= 1

print("Sol: ", sum([idx * int(val) for idx, val in enumerate(rep[:rep.index('.')])]))
