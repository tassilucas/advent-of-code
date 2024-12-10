
import random

results = []
eqs = []
ops = ['*', '+', '|']

tcr = 0

with open('input', 'r') as fp:
    for line in fp:
        val, eq = line.strip().split(":")
        results.append(int(val.strip()))
        eqs.append(eq.strip().split(" "))

for l, r in zip(eqs, results):
    tested = []
    poss = pow(3, len(l) - 1)
    gen = True
    
    # generating possibilites
    while gen:
        if len(tested) == poss:
            gen = False

        s = ''
        for n in range(len(l) - 1):
            s += ops[random.randint(0, 2)]

        if s not in tested:
            # solve generations
            ans = int(l[0])
            idx = 1
            for op in s:
                if op == '*':
                    ans = ans * int(l[idx])
                elif op == '+':
                    ans = ans + int(l[idx])
                elif op == '|':
                    ans = int(str(ans) + str(l[idx]))
                idx += 1

            if ans == r:
                tcr += r
                print(tcr)
                break

            tested.append(s)

print(tcr)
