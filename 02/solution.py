def readFile():
    text_file = open("./02/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(lines: list[str]):

    score = 0

    for line in lines:
        game = line.split(' ')
        a = ord(game[0]) - 65
        b = ord(game[1]) - 88
        score += gameWinner(a, b) + b + 1

    return score


def solve2(lines: list[str]):

    score = 0

    for line in lines:
        game = line.split(' ')
        a = ord(game[0]) - 65
        b = rightMove(a, game[1])
        score += gameWinner(a, b) + b + 1

    print(score)


def rightMove(va, b):
    vb = ord(b) - 89

    res = (va + vb) % 3
    return res


def gameWinner(a, b):
    res = b - a

    if res > 1:
        res -= 3
    elif res < -1:
        res += 3

    return (res + 1) * 3


if __name__ == '__main__':
    lines = readFile()
    solve2(lines)
