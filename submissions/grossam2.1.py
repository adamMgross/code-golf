def f(s):
    num=0
    for c in s:
        if c=='a':
            num+=2
        if c=='d':
            num-=1
        if c=='m':
            num*=2
        if c=='o':
            return num

i=open('problem1.final.txt', 'r')
o=open('grossam2.1.txt', 'w')
s=i.readline()
while s!='':
    o.write(str(f(s))+'\n')
    s=i.readline()
o.close()
i.close()
