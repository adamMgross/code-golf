def d(arr):
    rsum=0
    for i in range(0, len(arr)-1):
        rsum+=arr[i+1]-arr[i]
    return rsum

def f(num):
    r=[]
    for i in range(0, len(num)-1):
        r.append(int(num[i]))
    for i in range(1, len(num)):
        sum1=d(r[:i])
        sum2=d(r[i:])
        if sum1==sum2:
            return i


i=open('problem3.final.txt', 'r')
o=open('grossam2.3.txt', 'w')
s=i.readline()
while s!='':
    x=f(s)
    o.write(s[:x]+' '+s[x:])
    s=i.readline()
o.close()
i.close()
