import re
from sys import stdin


# Y = 10
# Z = 20
Y = 2000000
Z = 4000000


def main():
    t = []
    for l in stdin:
        l = l.strip()
        m = re.match(
            'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', l)
        if m:
            t.append((int(m.group(1)), int(m.group(2)),
                     int(m.group(3)), int(m.group(4))))

    l = []
    for o in t:
        d = abs(o[0]-o[2]) + abs(o[1]-o[3])
        if abs(Y-o[1]) <= d:
            e = d - abs(Y-o[1])
            if Y == o[3] and o[2] == o[0]:
                continue
            elif Y == o[3] and o[2] < o[0]:
                r = (o[0]-e+1, o[0]+e+1)
            elif Y == o[3] and o[2] > o[0]:
                r = (o[0]-e, o[0]+e)
            else:
                r = (o[0]-e, o[0]+e+1)
            l.append(r)

    def m(l):
        for i in range(len(l)):
            for j in range(len(l)):
                if i is not j:
                    if l[i][0] <= l[j][0] <= l[i][1] or l[i][0] <= l[j][1] <= l[i][1]:
                        r = (min(l[i][0], l[j][0]), max(l[i][1], l[j][1]))
                        l[j] = r
                        l.pop(i)
                        return True
        return False
    while m(l):
        pass
    print(sum(abs(x[0]-x[1]) for x in l))

    for y in range(Z+1):
        l = []
        for o in t:
            d = abs(o[0]-o[2]) + abs(o[1]-o[3])
            if abs(y-o[1]) <= d:
                e = d - abs(y-o[1])
                r = (o[0]-e, o[0]+e+1)
                l.append(r)

        def m(l):
            for i in range(len(l)):
                for j in range(len(l)):
                    if i is not j:
                        if l[i][0] <= l[j][0] <= l[i][1] or l[i][0] <= l[j][1] <= l[i][1]:
                            r = (min(l[i][0], l[j][0]), max(l[i][1], l[j][1]))
                            l[j] = r
                            l.pop(i)
                            return True
            return False
        while m(l):
            pass
        if len(l) > 1:
            l.sort()
            for i in range(1, len(l)):
                x = l[i-1][1]
                if 0 <= x <= Z:
                    print(x*4000000+y)
                    return


if __name__ == '__main__':
    main()
