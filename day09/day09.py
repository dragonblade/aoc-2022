import math
from sys import stdin


m = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}


def main():
    lines = [l for l in stdin]
    a(lines)
    b(lines)


def a(lines):
    v = set()
    hx, hy, tx, ty = 0, 0, 0, 0
    v.add((tx, ty))

    for line in lines:
        d, c = line.strip().split()
        for _ in range(int(c)):
            dx, dy = m[d]
            hx += dx
            hy += dy
            if abs(hx - tx) >= 2:
                tx += math.copysign(1, hx - tx)
                if hy != ty:
                    ty += math.copysign(1, hy - ty)
            elif abs(hy - ty) >= 2:
                ty += math.copysign(1, hy - ty)
                if hx != tx:
                    tx += math.copysign(1, hx - tx)
            v.add((tx, ty))
    print(len(v))


def b(lines):
    v = set()
    w = [(0, 0)]*10
    v.add((0, 0))
    for line in lines:
        d, c = line.strip().split()
        for _ in range(int(c)):
            hx, hy = w[0]
            dx, dy = m[d]
            w[0] = (hx + dx, hy + dy)
            for i in range(1, len(w)):
                px, py = w[i-1]
                sx, sy = w[i]
                if abs(px - sx) >= 2:
                    sx += math.copysign(1, px - sx)
                    if py != sy:
                        sy += math.copysign(1, py - sy)
                elif abs(py - sy) >= 2:
                    sy += math.copysign(1, py - sy)
                    if px != sx:
                        sx += math.copysign(1, px - sx)
                w[i] = (sx, sy)
            v.add(w[-1])
    print(len(v))


if __name__ == '__main__':
    main()
