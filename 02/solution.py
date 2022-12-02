

if __name__ == '__main__':
    s1 = sum([(((ord(g[1]) - 87 - ord(g[0]) - 65) %
                3) * 3 + ord(g[1]) - 87) for g in [l.split(' ') for l in open("./02/input.txt", "r").read().split('\n')]])
    s2 = sum([(((ord(g[0]) - 65 + ord(g[1]) - 89) % 3 - ord(g[0]) - 65 + 1) %
               3) * 3 + (ord(g[0]) - 65 + ord(g[1]) - 89) % 3 + 1 for g in [l.split(' ') for l in open("./02/input.txt", "r").read().split('\n')]])
    print(s1)
    print(s2)
