def f(n):
    if n==42:
        return 'yes'
    if n<42:
        return 'no'
    if n%2==0:
        return f(n/2)
    if n%3==0:
        l=n%10
        p=((n%100)/10)
        return f(-1+n-l*p)
    if n%5==0:
        return f(n-42)
    return f(n-1)

i=open('problem2.final.txt', 'r')
o=open('grossam2.2.txt', 'w')
s=i.readline()
while s!='':
    o.write(f(int(s))+'\n')
    s=i.readline()
o.close()
i.close()
