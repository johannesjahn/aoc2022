import re


class File:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.size = 0
        self.children = list()
        self.parent = parent


def parseInput(lines: list[str]):
    root = Directory('/', None)
    currentDir = root
    cmd = re.compile(r"\$ (.*)")
    file = re.compile(r"([0-9]+) (.+)")
    folder = re.compile(r"dir (.+)")
    currentCommand = ''
    for line in lines[1:]:
        cmdMatch = cmd.match(line)
        if (cmdMatch):
            currentCommand = ''
            if cmdMatch.groups()[0][:2] == 'cd':
                currentCommand = 'cd'
                ndir = cmdMatch.groups()[0][3:]
                if ndir == '..':
                    if currentDir.parent:
                        currentDir = currentDir.parent
                else:
                    m = [x for x in currentDir.children if x.name == ndir]
                    if len(m) > 0:
                        currentDir = m[0]
                    else:
                        d = Directory(ndir, currentDir)
                        currentDir.children.append(d)
                        currentDir = d
            elif cmdMatch.groups()[0][:2] == 'ls':
                currentCommand = 'ls'
            continue
        fileMatch = file.match(line)
        if (fileMatch):
            if currentCommand != 'ls':
                continue
            s = int(fileMatch.groups()[0])
            n = fileMatch.groups()[1]
            m = [x for x in currentDir.children if x.name == n]
            if len(m) > 0:
                m[0].size = s
            else:
                currentDir.children.append(File(s, n))
            continue
        folderMatch = folder.match(line)
        if folderMatch:
            if currentCommand != 'ls':
                continue
            n = folderMatch.groups()[0]
            m = [x for x in currentDir.children if x.name == n]
            if len(m) == 0:
                d = Directory(n, currentDir)
                currentDir.children.append(d)
            continue
    return root


def calculateFolderSizes(d: Directory):
    res = 0
    for c in d.children:
        if type(c) is Directory:
            res += calculateFolderSizes(c)
        else:
            res += c.size
    d.size = res
    return res


def readFile():
    text_file = open("./07/input.txt", "r")
    lines = text_file.read().split('\n')
    return lines


def solve1(d: Directory):
    res = 0
    for c in d.children:
        if type(c) is Directory:
            res += solve1(c)
    if d.size <= 100000:
        res += d.size
    return res


def getAllDirs(d: Directory):
    res = list()
    for c in d.children:
        if type(c) is Directory:
            ds = getAllDirs(c)
            for dss in ds:
                res.append(dss)
    res.append(d)
    return res


def solve2(d: Directory):
    unused_space = 70000000 - d.size
    space_to_be_freed = 30000000 - unused_space
    allDirs = getAllDirs(d)
    newlist = sorted(allDirs, key=lambda x: x.size)
    for ds in newlist:
        if ds.size >= space_to_be_freed:
            return ds.size


if __name__ == '__main__':
    lines = readFile()
    d = parseInput(lines)
    calculateFolderSizes(d)
    print(solve1(d))
    print(solve2(d))
