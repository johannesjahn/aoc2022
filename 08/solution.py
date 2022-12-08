from collections import Counter


def readFile():
    text_file = open("./08/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):
    trees = [[*map(int, line)] for line in lines]

    n = 2 * (len(trees[0]) + len(trees) - 2)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            tree = trees[y][x]

            row = trees[y]
            col = [i[x] for i in trees]

            left = row[:x]
            right = row[x + 1:]
            top = col[:y]
            bottom = col[y + 1:]

            if tree > min(max(left), max(right), max(top), max(bottom)):
                n += 1

    return n


def solve2(lines: list[str]):
    trees = [[*map(int, line)] for line in lines]

    s = 0
    w = len(trees[0])
    h = len(trees)

    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            t = trees[y][x]

            row = trees[y]
            col = [i[x] for i in trees]

            left = row[:x][::-1]
            right = row[x + 1:]
            top = col[:y][::-1]
            bottom = col[y + 1:]

            left_blocked = [i for i, v in enumerate(left) if v - t >= 0]
            left_score = x if len(left_blocked) == 0 else left_blocked[0] + 1

            right_blocked = [i for i, v in enumerate(right) if v - t >= 0]
            right_score = w - x - \
                1 if len(right_blocked) == 0 else right_blocked[0] + 1

            top_blocked = [i for i, v in enumerate(top) if v - t >= 0]
            top_score = y if len(top_blocked) == 0 else top_blocked[0] + 1

            bottom_blocked = [i for i, v in enumerate(bottom) if v - t >= 0]
            bottom_score = h - y - \
                1 if len(bottom_blocked) == 0 else bottom_blocked[0] + 1

            ss = left_score * right_score * top_score * bottom_score
            if ss > s:
                s = ss

    return s


if __name__ == '__main__':
    lines = readFile()
    print(solve1(lines))
    print(solve2(lines))
