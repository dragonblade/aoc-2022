from sys import stdin


def main():
    sa = 0
    sb = 0

    for line in stdin:
        line = line.strip()
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))

        if a1 <= b1 and b2 <= a2:
            sa += 1
        elif b1 <= a1 and a2 <= b2:
            sa += 1

        if a2 >= b1 and a1 <= b2:
            sb += 1

    print(sa)
    print(sb)


if __name__ == '__main__':
    main()
