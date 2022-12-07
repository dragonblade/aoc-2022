from sys import stdin


def main():
    t = {}
    c = t

    for line in stdin:
        line = line.strip()

        if line.startswith('$ cd'):
            n = line[5:]
            if n == '/':
                c = t
            else:
                c = c[n]
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            n = line[4:]
            c[n] = {'..': c}
        else:
            s, n = line.split()
            c[n] = int(s)

    print(a(t)[1])
    s, l = b(t)
    m = 30000000 - (70000000 - s)
    print(min(filter(lambda x: x >= m, l)))


def a(t):
    s, f = 0, 0
    for k, v in t.items():
        if k == '..':
            continue
        elif type(v) == dict:
            x, y = a(v)
            s += x
            f += y
        else:
            s += v
    if s <= 100000:
        f += s
    return s, f


def b(t):
    s, l = 0, []
    for k, v in t.items():
        if k == '..':
            continue
        elif type(v) == dict:
            x, y = b(v)
            s += x
            l.extend(y)
        else:
            s += v
    l.append(s)
    return s, l


if __name__ == '__main__':
    main()
