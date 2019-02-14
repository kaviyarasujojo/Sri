a=int(input())
d=''
if(a>1):
    for i in range(1,a+1):
        c=a%i
        if(c==0):
            d=d+str(i)+" "
print(d)
