def readFile():
    text_file = open("./01/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve(lines: list[str]):
    return 7


if __name__ == '__main__':
    lines = readFile()
    solve(lines)
