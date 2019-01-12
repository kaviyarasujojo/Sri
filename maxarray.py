a=int(input())
b=1
d=1
while (b<=a):
    c=int(input())
    if (c>=d):
        max=c
    else:
        max=d
    e=max
    d=e
    b=b+1
print(max)
