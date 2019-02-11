a=input()
c=0
for i in a:
    if(0<=int(i)<=1):
        c+=1
if(int(len(a))==c):
    print("yes")
else:
    print("no")
