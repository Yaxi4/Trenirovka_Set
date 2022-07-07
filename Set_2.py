a = input()
a = list(a)
b = '1234567890'
c = set()
s = {}
d=[]
for i in a:
    if i in b:
        d.append(int(i))
d.sort()
for i in range(1,len(d)):
    if d[i-1]==d[i]:
        c.add(d[i])
if len(c)>0:
    print(*c)
else:
    print('NO')

