a=int(input())
d=0
if(a>1):
    for i in range(1,a+1):
        c=a%i
        if(c==0):
            d+=1
if(d>2):
    print("yes")
else:
    print("no")
