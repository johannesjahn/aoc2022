import re


def readFile():
    text_file = open("./05/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    stacks = []
    for i in range(int((len(lines[0]) + 1) / 4)):
        stacks.append([])
    for idx, line in enumerate(lines):
        if (line[1] == '1'):
            break
        i = 1
        while (i < len(line)):
            if (line[i] != ' '):
                stacks[int((i - 1) / 4)].insert(0, line[i])
            i += 4

    idx = idx + 2
    reg = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    while (idx < len(lines)):
        m = reg.match(lines[idx]).groups()
        amount = int(m[0])
        f = int(m[1])
        t = int(m[2])

        for i in range(amount):
            if len(stacks[f - 1]) == 0:
                break
            v = stacks[f - 1][-1]
            del stacks[f - 1][-1]
            stacks[t - 1].append(v)

        idx += 1

    return ''.join([x[-1] for x in stacks])


def solve2(lines: list[str]):
    stacks = []
    for i in range(int((len(lines[0]) + 1) / 4)):
        stacks.append([])
    for idx, line in enumerate(lines):
        if (line[1] == '1'):
            break
        i = 1
        while (i < len(line)):
            if (line[i] != ' '):
                stacks[int((i - 1) / 4)].insert(0, line[i])
            i += 4

    idx = idx + 2
    reg = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    while (idx < len(lines)):
        m = reg.match(lines[idx]).groups()
        amount = int(m[0])
        f = int(m[1])
        t = int(m[2])

        ms = []
        for i in range(amount):
            if len(stacks[f - 1]) == 0:
                break
            ms.append(stacks[f - 1][-1])
            del stacks[f - 1][-1]

        ms.reverse()
        for c in ms:
            stacks[t - 1].append(c)
        idx += 1

    return ''.join([x[-1] for x in stacks])


if __name__ == '__main__':
    lines = readFile()
    print(solve1(lines))
    print(solve2(lines))
