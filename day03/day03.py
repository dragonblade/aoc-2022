from sys import stdin


P = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    sa = 0
    sb = 0

    g = []

    for line in stdin:
        line = line.strip()
        a, b = line[0:len(line)//2], line[len(line)//2:]

        g.append(line)

        for c in set(list(b)):
            if c in a:
                sa += P.index(c)

        if len(g) == 3:
            a, b, c, g = *map(set, map(list, g)), []
            t = a & b & c
            sb += P.index(t.pop())

    print(sa)
    print(sb)


if __name__ == '__main__':
    main()
