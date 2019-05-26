a=input()
b=a.lower()
c=0
d=0
for i in range(len(a)):
    if b.count(b[i])>c:
        c=b.count(b[i])
        d=i
print(a[d])
