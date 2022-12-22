from sys import stdin


def main():
    g = []
    for line in stdin:
        line = line.strip()
        g.append(list(map(int, line)))
    m = [[False]*len(x) for x in g]

    sa = (len(g) + len(g[0])) * 2 - 4
    for x in range(1, len(g[0])-1):
        sa += a(g, m, x, 0, 0, 1)
        sa += a(g, m, x, len(g)-1, 0, -1)
    for y in range(1, len(g)-1):
        sa += a(g, m, 0, y, 1, 0)
        sa += a(g, m, len(g[0])-1, y, -1, 0)
    print(sa)

    sb = 0
    for x in range(len(g[0])):
        for y in range(len(g)):
            s = 1
            s *= b(g, x, y, 1, 0)
            s *= b(g, x, y, -1, 0)
            s *= b(g, x, y, 0, 1)
            s *= b(g, x, y, 0, -1)
            sb = max(sb, s)
    print(sb)


def a(g, m, sx, sy, dx, dy):
    s = 0
    p = g[sy][sx]
    x = sx + dx
    y = sy + dy
    while 1 <= x < len(g[0])-1 and 1 <= y < len(g)-1:
        if g[y][x] > p:
            p = g[y][x]
            if not m[y][x]:
                m[y][x] = True
                s += 1
        x += dx
        y += dy
    return s


def b(g, x, y, dx, dy):
    s = 0
    h = g[y][x]
    x += dx
    y += dy
    while 0 <= x < len(g[0]) and 0 <= y < len(g):
        s += 1
        if g[y][x] >= h:
            break
        x += dx
        y += dy
    return s


if __name__ == '__main__':
    main()
