a=input()
b=len(a)
c=[]
for i in a:
    c.append(i)
if(b%2==0):
    c[b//2]="*"
    c[(b//2)-1]="*"
else:
    c[b//2]="*"
a=''
for i in c:
    a=a+i
print(a)
    
