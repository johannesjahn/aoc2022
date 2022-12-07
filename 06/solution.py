from collections import Counter


def readFile():
    text_file = open("./06/input.txt", "r")
    lines = text_file.read()
    return lines


def solve1(lines: list[str]):
    for i in range(len(lines) - 3):
        buffer = lines[i: i + 4]
        if len(Counter(buffer)) == 4:
            return i + 4


def solve2(lines: list[str]):
    for i in range(len(lines) - 13):
        buffer = lines[i: i + 14]
        if len(Counter(buffer)) == 14:
            return i + 14


if __name__ == '__main__':
    lines = readFile()
    print(solve1(lines))
    print(solve2(lines))
