import math
from sys import stdin


def main():
    i = list(stdin)
    q(i[:], 3, 20)
    q(i[:], 1, 10_000)


def q(i, w, r):
    t = []
    while len(i):
        if i.pop(0).startswith('Monkey'):
            s = eval(f'[{i.pop(0).split(":")[1].strip()}]')
            e = i.pop(0).split('=')[1].strip()
            c = int(i.pop(0).split()[-1].strip())
            p = int(i.pop(0).split()[-1].strip())
            n = int(i.pop(0).split()[-1].strip())
            t.append({'s': s, 'e': e, 'c': c, 'p': p, 'n': n, 'i': 0})
    for _ in range(r):
        for m in range(len(t)):
            while len(t[m]['s']):
                t[m]['i'] += 1
                old = t[m]['s'].pop(0)
                n = (eval(t[m]['e']) // w) % (2 *
                                              3 * 5 * 7 * 11 * 13 * 17 * 19)
                if n % t[m]['c'] == 0:
                    d = t[m]['p']
                else:
                    d = t[m]['n']
                t[d]['s'].append(n)
    print(math.prod(sorted([x['i'] for x in t])[-2:]))


if __name__ == '__main__':
    main()
