a=input()
b=set()
from string import ascii_lowercase
for i in a:
    if i in ascii_lowercase:
        b.add(i)
print(len(b))