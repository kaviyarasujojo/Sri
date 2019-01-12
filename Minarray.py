a=int(input())
b=1
d=1
while (b<=a):
    c=int(input())
    if (c<=d):
        min=c
    else:
        min=d
    e=min
    d=e
    b=b+1
print(min)
