l1 = []
l2 = []

def read_file():
    with open('input', 'r') as fp:
        for line in fp:
            line = line.strip()
            l1.append(int(line.split(" ")[0]))
            l2.append(int(line.split(" ")[-1]))

def sum_distances():
    # sorting distances
    l1.sort()
    l2.sort()

    distances = []

    for idx, elm in enumerate(l1):
        distances.append(abs(elm - l2[idx]))

    return sum(distances)

read_file()
res = sum_distances()
print(f"Solution: {res}")
