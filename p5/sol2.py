
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

def fix_page(page):
    tail = []
    curr = page
    ptr = 0
    reset = False
    
    while ptr < len(page):
        if curr[ptr] in rules:
            ptr_rules = rules[curr[ptr]]
            wrongs = list(set(ptr_rules) & set(tail))

            if len(wrongs) > 0:
                wrong_idx = wrongs.index(wrongs[-1])
                tmp = curr[wrong_idx]
                curr[wrong_idx] = curr[ptr]
                curr[ptr] = tmp
                reset = True

        if reset:
            tail = []
            ptr = 0
            reset = False
        else:
            tail.append(curr[ptr])
            ptr += 1

    return curr

def sum_middles():
    ans = 0
    for page in pages:
        if not check_ordering(page):
            fixed_page = fix_page(page)
            mid = len(fixed_page) // 2
            ans += int(fixed_page[mid])

    return ans

print(sum_middles())
