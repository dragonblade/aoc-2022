from sys import stdin


def main():
    c = 0
    l = []

    for line in stdin:
        line = line.strip()
        if not line:
            l.append(c)
            c = 0
        else:
            c += int(line)

    print(max(l))
    print(sum(sorted(l)[-3:]))


if __name__ == '__main__':
    main()
