def readFile():
    text_file = open("./01/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    print(lines)

    res = list()
    currIndex = 0
    res.append(0)

    for i in range(len(lines)):
        if lines[i] == '':
            currIndex += 1
            res.append(0)
            continue
        res[currIndex] += int(lines[i])

    res.sort()
    print(max(res))

def solve2(lines: list[str]):
    print(lines)

    res = list()
    currIndex = 0
    res.append(0)

    for i in range(len(lines)):
        if lines[i] == '':
            currIndex += 1
            res.append(0)
            continue
        res[currIndex] += int(lines[i])

    res.sort()
    print(res[-1] + res[-2] + res[-3])



if __name__ == '__main__':
    lines = readFile()
    solve2(lines)
