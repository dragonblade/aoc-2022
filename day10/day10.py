from sys import stdin


def main():
    c = [1]
    r = 1
    for line in stdin:
        line = line.strip()
        c.append(r)
        if line.startswith('noop'):
            pass
        elif line.startswith('addx'):
            c.append(r)
            r += int(line[5:])

    print(sum(c[x]*x for x in range(20, 221, 40)))
    for i, v in enumerate(c[1:]):
        if i % 40 == 0:
            print()
        if v - 1 <= (i % 40) <= v + 1:
            print(end='#')
        else:
            print(end='.')


if __name__ == '__main__':
    main()
