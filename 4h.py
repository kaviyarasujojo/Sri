a=int(input())
b=input().split()
for i in b:
    if b.count(i)==1:
        print(i)
        break
