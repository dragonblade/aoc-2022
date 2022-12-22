from sys import stdin


def v(x):
    if x == 'S':
        return ord('a')
    elif x == 'E':
        return ord('z')
    else:
        return ord(x)


def f(g, s):
    h = []
    q = [(0, s)]
    while len(q):
        c, p = q.pop(0)
        if p in h:
            continue
        h.append(p)
        x, y = p
        if g[y][x] == 'E':
            return c
        if x - 1 >= 0 and v(g[y][x-1]) <= v(g[y][x]) + 1:
            q.append((c+1, (x-1, y)))
        if x + 1 < len(g[0]) and v(g[y][x+1]) <= v(g[y][x]) + 1:
            q.append((c+1, (x+1, y)))
        if y - 1 >= 0 and v(g[y-1][x]) <= v(g[y][x]) + 1:
            q.append((c+1, (x, y-1)))
        if y + 1 < len(g) and v(g[y+1][x]) <= v(g[y][x]) + 1:
            q.append((c+1, (x, y+1)))
    return False


def main():
    s = (0, 0)
    g = []
    for line in stdin:
        line = list(line.strip())
        if line.count('S') > 0:
            s = (line.index('S'), len(g))
        if line.count('E') > 0:
            e = (line.index('E'), len(g))
        g.append(line)

    print(f(g, s))

    l = []
    for y in range(len(g)):
        for x in range(len(g[0])):
            if v(g[y][x]) == ord('a'):
                l.append(f(g, (x, y)))
    print(min(x for x in l if x))


if __name__ == '__main__':
    main()
