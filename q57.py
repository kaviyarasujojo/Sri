a,b=input().split()
d=[]
e=0
for i in range(int(a)):
    c=int(input())
    d.append(c)
for i in range(int(a)):
    if(d[i]==int(b)):
        e+=1
print(e)
