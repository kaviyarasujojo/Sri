a=int(input())
b=[]
d=0
e=0
for i in range(a):
    c=input()
    b.append(c)
for i in b:
    for y in i:
        d+=ord(y)
    if d==612:
        e+=1
    d=0
print(e)
