import sys; p = sys.argv[1]
def w(c):
    s = sys.stdout;s.write(str(c));s.flush()
cp, dp, d, j = 0, 0, [0], []
while cp < len(p):
    x = p[cp]
    if x == '>':
        d.append(0)
        dp += 1
    elif x == '<':
        d = [0] + d
    elif x == '+':
        d[dp] += 1
    elif x == '-':
        d[dp] -= 1
    elif x == '.':
        w((d[dp]))
    elif x == ',':
        d[dp] = (input('>'))
    elif x == '[':
        if d[dp] == 0:
            c = 1
            while True:
                cp += 1
                if p[cp] == '[':
                    c += 1
                elif p[cp] == ']':
                    c -= 1
                    if c == 0:
                        break
    elif x == ']':
        if d[dp] != 0:
            c = 1
            while True:
                cp -= 1
                if p[cp] == ']':
                    c += 1
                elif p[cp] == '[':
                    c -= 1
                    if c == 0:
                        break
    cp += 1
