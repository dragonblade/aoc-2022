from sys import stdin


def main():
    o, g = 500, [['+']]
    for l in stdin:
        s = [[int(y.strip()) for y in x.split(',')]
             for x in l.strip().split('->')]
        n = min(x[0] for x in s)
        if n < o:
            g = [['.']*(o-n) + r for r in g]
            o = n
        n = max(x[0] for x in s)
        if n >= o + len(g[0]):
            g = [r + ['.']*(n-o-len(g[0])+1) for r in g]
        n = max(x[1] for x in s)
        while n >= len(g):
            g.append(['.']*len(g[0]))
        for i in range(1, len(s)):
            a, b = s[i-1], s[i]
            if a[0] == b[0]:
                x = a[0]
                r = sorted([a[1], b[1]])
                for y in range(r[0], r[1]+1):
                    g[y][x-o] = '#'
            else:
                y = a[1]
                r = sorted([a[0], b[0]])
                for x in range(r[0], r[1]+1):
                    g[y][x-o] = '#'

    i = 0
    try:
        while True:
            x, y = 500, 0
            while True:
                if g[y+1][x-o] == '.':
                    y += 1
                elif g[y+1][x-o-1] == '.':
                    x -= 1
                    y += 1
                elif g[y+1][x-o+1] == '.':
                    x += 1
                    y += 1
                else:
                    break
            g[y][x-o] = 'o'
            i += 1
    except IndexError:
        pass
    print(i)

    g.append(['.']*len(g[0]))
    g.append(['#']*len(g[0]))
    while True:
        x, y = 500, 0
        while True:
            if x - 1 <= o:
                g = [['.'] + r for r in g]
                g[-1][0] = '#'
                o -= 1
            if x + 1 >= o + len(g[0]):
                g = [r + ['.'] for r in g]
                g[-1][-1] = '#'
            if g[y+1][x-o] == '.':
                y += 1
            elif g[y+1][x-o-1] == '.':
                x -= 1
                y += 1
            elif g[y+1][x-o+1] == '.':
                x += 1
                y += 1
            else:
                break
        g[y][x-o] = 'o'
        i += 1
        if x == 500 and y == 0:
            break
    print(i)


if __name__ == '__main__':
    main()
