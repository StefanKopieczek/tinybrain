import sys;p=sys.argv[1];
def w(c): s=sys.stdout;s.write(str(c)+' ');s.flush()
i,j,d,g=0,0,[0],[]
while i<len(p):
    switch=0
    x,y=p[i],d[j]
    if x=='>':d.append(0);j+=1
    elif x=='<':d=[0]+d
    elif x=='+':d[j]+=1
    elif x=='-':d[j]-=1
    elif x=='.':w(d[j])
    elif x==',':d[j]=(input('>'))
    elif x == '[':
        switch = 1
    elif x == ']':
        switch = -1


    if switch != 0:
        if (switch==1 and y==0) or (switch==-1 and y != 0):
            c=1
            l,r = ('[',']') if switch==1 else (']','[')
            while True:
                i+=switch
                if p[i] == l:
                    c += 1
                elif p[i] == r:
                    c -= 1
                    if c == 0: break
    i += 1
