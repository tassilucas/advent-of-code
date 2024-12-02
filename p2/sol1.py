
reports = []

def read_file():
    with open('input', 'r') as fp:
        for line in fp:
            reports.append([int(x) for x in line.strip().split(' ')])

def analyse_report(report):
    # mark if is descending or ascending
    ascending = False
    if report[0] > report[1]:
        ascending = False
    elif report[0] < report[1]:
        ascending = True
    else:
        return False

    last = report[0]
    safe = True
    for level in report[1:]:
        # last < level
        if ascending:
            if level <= last or (level - last < 1 or level - last > 3):
                safe = False
        # last > level 
        else:
            if level >= last or (last - level < 1 or last - level > 3):
                safe = False

        last = level

    return safe

def analyse_safety():
    analysis = []

    for report in reports:
        r = analyse_report(report)
        analysis.append(r)

    return analysis

read_file()
res = analyse_safety().count(True)
print(f"Solution: {res}")
