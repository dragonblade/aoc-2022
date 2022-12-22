from sys import stdin


def main():
    sa = 0
    sb = 0

    line = list(input().strip())

    i = 0
    while len(set(line[i:i+4])) != 4:
        i += 1
    sa = i + 4

    i = 0
    while len(set(line[i:i+14])) != 14:
        i += 1
    sb = i + 14

    print(sa)
    print(sb)


if __name__ == '__main__':
    main()
