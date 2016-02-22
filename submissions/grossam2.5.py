def f(s, res):
    if s==0:
        return res
    if s%2==1:
        return f(s+1,"d"+res)
    if (s/2)%2==0 or s < 0:
        return f(s/2,"m"+res)
    return f(s-2,"a"+res)

i=open('problem5.final.txt', 'r')
o=open('grossam2.5.txt', 'w')
s=i.readline()
while s!='':
    o.write(str(f(int(s),'o\n')))
    s=i.readline()
o.close()
i.close()
