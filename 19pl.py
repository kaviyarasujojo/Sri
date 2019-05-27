a=int(input())
c=0
d=''
for i in range(2,a+1):
    if a%i==0:
        b=1
        while b<=i:
            if i%b==0:
                c+=1
            b+=1
        if c==2:
            d+=str(i)+" "
        c=0
print(d)
