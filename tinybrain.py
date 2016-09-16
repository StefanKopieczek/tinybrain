import sys;p=sys.argv[1];
def w(c): s=sys.stdout;s.write(str(c)+' ');s.flush()
i,j,d,g=0,0,[0],[]
while i<len(p):
    s=0
    x,y=p[i],d[j]
    if x=='>':d.append(0);j+=1
    elif x=='<':d=[0]+d
    elif x=='+':d[j]+=1
    elif x=='-':d[j]-=1
    elif x=='.':w(d[j])
    elif x==',':d[j]=(input('>'))
    elif x=='[':s=1
    elif x==']':s=-1
    if s != 0:
        if (s==1 and y==0) or (s==-1 and y != 0):
            c=1
            l,r=('[',']') if s==1 else (']','[')
            while True:
                i+=s
                if p[i]==l:c+=1
                elif p[i]==r:
                    c -= 1
                    if c == 0: break
    i+=1
