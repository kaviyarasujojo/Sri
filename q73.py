a=int(input())
b,c=input().split()
d=[]
for i in range(int(b)+1,int(c)):
    if int(i)==a:
        d.append(i)
        break
    else:
        i=i+1
if (len(d))>0:
    print("yes")
else:
    print("no")
