a=input()
b=[]
c=''
for i in a:
    b.append(i)
b.reverse()
for i in b:
    c=c+i
if (a==c):
    print("yes")
else:
    print("no")

