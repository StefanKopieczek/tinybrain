import sys;p=sys.argv[1]
def w(c):s=sys.stdout;s.write(str(c)+' ');s.flush()
i=j=0;d=[0];a=abs;b=bool
while i<len(p):
 s=0;x,y=p[i],d[j]
 if x=='>':d.append(0);j+=1
 elif x=='<':d=[0]+d
 elif x in '+-':d[j]+=(-1,1)[x=='+']
 elif x=='.':w(d[j])
 elif x==',':d[j]=(input('>'))
 elif x in '[]':s=(1,-1)[x==']']
 if s!=0 and b(s+1)!=b(y):
  c=1;l,r=('[',']') if s==1 else (']','[')
  while 1:
   i+=s
   if p[i]==l:c+=1
   elif p[i]==r:
    c-=1
    if c==0:break
 i+=1
