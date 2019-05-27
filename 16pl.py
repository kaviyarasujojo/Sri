a=int(input())
b=[]
b=input().split()
for i in range(len(b)):
    if b.count(b[i])==1:
        print(b[i])
        break
