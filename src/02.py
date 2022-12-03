from sys import stdin


TBL_A = [
    [],
    [0, 3, 6, 0],
    [0, 0, 3, 6],
    [0, 6, 0, 3],
]
TBL_B = [
    [],
    [0, 3, 1, 2],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
]


def main():
    sa = 0
    sb = 0

    for line in stdin:
        a, b = line.strip().split()
        a, b = ord(a) - 64, ord(b) - 87

        sa += b
        sa += TBL_A[a][b]

        sb += [0, 0, 3, 6][b]
        sb += TBL_B[a][b]

    print(sa)
    print(sb)


if __name__ == '__main__':
    main()
