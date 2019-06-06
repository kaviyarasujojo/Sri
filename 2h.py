a=int(input())
b=input().split()
b.sort(reverse=True,key=int)
c=''
for i in b:
    c+=i
print(c)
