
rules = {}
pages = []

with open('input', 'r') as fp:
    state = True
    for line in fp:
        if len(line.strip()) > 5:
            pages.append(line.strip().split(','))
        elif line.strip() != '':
            k, v = line.strip().split('|')
            if k in rules:
                rules[k].append(v)
            else:
                rules[k] = [v]

def check_ordering(page):
    tail = []

    for ptr in page:
        if ptr in rules:
            ptr_rules = rules[ptr]
            if len(list(set(tail) & set(ptr_rules))) > 0:
                return False

        tail.append(ptr)

    return True

def sum_middles():
    ans = 0
    for page in pages:
        if check_ordering(page):
            mid = len(page) // 2
            ans += int(page[mid])

    return ans

print(sum_middles())
