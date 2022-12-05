

def readFile():
    text_file = open("./06/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    pass


def solve2(lines: list[str]):
    pass


if __name__ == '__main__':
    lines = readFile()
    print(solve1(lines))
    print(solve2(lines))
