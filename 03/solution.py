def readFile():
    text_file = open("./03/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    res = 0
    for r in lines:
        dp1 = r[0:int(len(r)/2)]
        dp2 = r[int(len(r)/2):]
        found = False
        for c in dp1:
            if c in dp2 and not found:
                res += ctv(c)
                found = True

    return res


def solve2(lines: list[str]):
    res = 0
    p = 0
    while p < len(lines):
        r1 = lines[p]
        r2 = lines[p + 1]
        r3 = lines[p + 2]
        for c in r1:
            if c in r2 and c in r3:
                res += ctv(c)
                break
        p += 3

    return res


def ctv(c: str) -> int:
    v = ord(c) - 96
    if v < 0:
        v += 58
    return v


if __name__ == '__main__':
    lines = readFile()
    print(solve2(lines))
