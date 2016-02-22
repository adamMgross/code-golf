def e(s):
    cs={}
    for c in s:
        if c not in cs:
            cs[c]=1
        else:
            cs[c]+=1
    od=0
    for c in cs:
        if cs[c]%2!=0:
            od+=1
            if od>1:
                return 'no'
    return 'yes'

i=open('problem4.final.txt', 'r')
o=open('grossam2.4.txt', 'w')
s=i.readline()
while s!='':
    o.write(e(s[:-1]) + '\n')
    s=i.readline()
o.close()
i.close()
