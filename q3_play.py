a=int(input())
b=''
c=True
for i in range(len(str(a))):
       c=a%10
       b=b+str(c)
       a=a//10
print(b)
