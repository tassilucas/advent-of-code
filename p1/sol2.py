l1 = []
l2 = []

def read_file():
    with open('input', 'r') as fp:
        for line in fp:
            line = line.strip()
            l1.append(int(line.split(" ")[0]))
            l2.append(int(line.split(" ")[-1]))

def similarity_score():
    r = {k: l2.count(k) for k in l1}
    return sum([k * v for k, v in r.items()])

read_file()
res = similarity_score()
print(f"Solution: {res}")
