vfibs={0: 0, 1: 1, 2: 1}

def vfib(x):
    if x in vfibs:
        return vfibs[x]
    n=vfibs[x-1]+vfibs[x-2]+vfibs[x-3]
    vfibs[x]=n
    return n

i=open('problem6.final.txt', 'r')
o=open('grossam2.6.txt', 'w')
s=i.readline()
while s!='':
    n =fibn=rsum=0
    while fibn<int(s):
        if fibn%3==0:
            rsum+=fibn
        n+=1
        fibn = vfib(n)
    o.write(str(rsum)+'\n')
    s=i.readline()
o.close()
i.close()
