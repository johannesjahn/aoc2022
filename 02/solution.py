def readFile():
    text_file = open("./02/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    print(lines)


def solve2(lines: list[str]):
    pass


if __name__ == '__main__':
    lines = readFile()
    solve2(lines)
