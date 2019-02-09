a,b=input().split()
c=[]
c=input().split()
e=0
for i in range(1,int(a)+1):
    if(int(c[i-1])==int(b)):
        e+=1
print(e)
