import copy
import re
from sys import stdin


def main():
    b = False
    ca = []
    cb = []

    for line in stdin:
        if line.strip().startswith('1'):
            b = True
            cb = copy.deepcopy(ca)
        elif not b:
            line = list(line.rstrip())
            i = 0
            while line:
                if line[0] == '[':
                    while i >= len(ca):
                        ca.append([])
                    ca[i] = [line[1]] + ca[i]
                line = line[4:]
                i += 1
        else:
            m = re.match('move (\d+) from (\d+) to (\d+)', line)
            if m:
                c = int(m.group(1))
                f = int(m.group(2)) - 1
                t = int(m.group(3)) - 1
                for _ in range(c):
                    ca[t].append(ca[f].pop())
                cb[f], s = cb[f][:-c], cb[f][-c:]
                cb[t].extend(s)

    print(''.join(x.pop() for x in ca))
    print(''.join(x.pop() for x in cb))


if __name__ == '__main__':
    main()
