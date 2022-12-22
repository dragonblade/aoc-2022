from functools import cmp_to_key
from sys import stdin


def c(a, b):
    a, b = a[:], b[:]
    while len(a) and len(b):
        x, y = a.pop(0), b.pop(0)
        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return 1
            elif x > y:
                return -1
        else:
            if isinstance(x, int):
                x = [x]
            if isinstance(y, int):
                y = [y]
            r = c(x, y)
            if r == 1:
                return 1
            elif r == -1:
                return -1
    if len(a) == 0:
        if len(b) == 0:
            return 0
        return 1
    return -1


def main():
    i, s = 0, 0
    l = list(stdin)
    m = [eval(x) for x in l if x.startswith('[')]

    while len(l):
        a = l.pop(0).strip()
        if a.startswith('['):
            i += 1
            a = eval(a)
            b = eval(l.pop(0).strip())
            if c(a, b) == 1:
                s += i
    print(s)

    m.append([[2]])
    m.append([[6]])
    m.sort(key=cmp_to_key(c), reverse=True)
    print((m.index([[2]])+1) * (m.index([[6]])+1))


if __name__ == '__main__':
    main()
