# put your python code here
a=map(int,input().split())
b=map(int,input().split())
a=set(a)
b=set(b)
c=a-b
c=list(c)
c.sort()
for i in c:
    print(i,end=' ')



