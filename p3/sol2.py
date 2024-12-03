
import re

code_input = ''

with open('input', 'r') as fp:
    code_input = ''.join(fp.read().strip().split('\n'))

def remove_disabled(insts):
    end = []
    enabled = True

    for inst in insts:
        if inst == "don't()":
            enabled = False
        elif inst == "do()":
            enabled = True
        elif enabled:
            end.append(inst)

    return end

def solve_mults():
    pattern = r'mul\([0-9][0-9]?[0-9]?\,[0-9][0-9]?[0-9]?\)|don\'t\(\)|do\(\)'
    mults = remove_disabled(re.findall(pattern, code_input))
    ans = 0
    for mult in mults:
        n1 = int(mult.split('(')[1].split(',')[0])
        n2 = int(mult.split('(')[1].split(',')[1][:-1])
        ans += n1*n2

    return ans

res = solve_mults()
print(f"Solution: {res}")
