a=int(input())
b=''
for i in range(2,a,2):
    if a%i==0:
        b+=str(i)+" "
print(b+str(a))
