import sys

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

# from https://stackoverflow.com/questions/17870544/find-starting-and-ending-indices-of-sublist-in-list,
# too lazy to create a function that matches the first sublist
# in a list (index() only works for strings).
def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind

ptr = len(rep) - 1
curr_id = rep[-1]
cnt = 0

while ptr >= 0:
    if rep[ptr] != curr_id:
        try:
            slot = find_sub_list(['.'] * cnt, rep)

            if slot <= ptr:
                frag = rep[ptr+1:ptr+1+cnt]
                rep[slot:slot+cnt] = frag
                rep[ptr+1:ptr+1+cnt] = ['.'] * cnt
        except:
            pass

        while rep[ptr] == '.':
            ptr -= 1
        curr_id = rep[ptr]
        cnt = 0
    else:
        cnt += 1
        ptr -= 1

print("Sol:", sum([idx * int(rep[idx]) for idx, _ in enumerate(rep) if rep[idx] != '.']))
