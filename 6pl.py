a,b=input().split()
c=[]
if(len(a)!=len(b)):
    print("no")
else:
    for i in range(len(a)):
        if a[i] in c:
            continue
        else:
            b=b.replace(b[i],a[i])
            c.append(a[i])
    if b==a:
        print("yes")
    else:
        print("no")
