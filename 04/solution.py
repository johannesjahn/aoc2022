def readFile():
    text_file = open("./04/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    res = 0
    for p in lines:
        e0 = p.split(',')[0]
        e1 = p.split(',')[1]
        e0_min = int(e0.split('-')[0])
        e0_max = int(e0.split('-')[1])
        e1_min = int(e1.split('-')[0])
        e1_max = int(e1.split('-')[1])
        if e0_min <= e1_min and e1_max <= e0_max:
            res += 1
            continue
        if e1_min <= e0_min and e0_max <= e1_max:
            res += 1
    return res


def solve2(lines: list[str]):
    res = 0
    for p in lines:
        e0 = p.split(',')[0]
        e1 = p.split(',')[1]
        e0_min = int(e0.split('-')[0])
        e0_max = int(e0.split('-')[1])
        e1_min = int(e1.split('-')[0])
        e1_max = int(e1.split('-')[1])
        if e0_min >= e1_min and e0_min <= e1_max:
            res += 1
            continue
        if e1_min >= e0_min and e1_min <= e0_max:
            res += 1
    return res


if __name__ == '__main__':
    lines = readFile()
    print(solve1(lines))
    print(solve2(lines))
