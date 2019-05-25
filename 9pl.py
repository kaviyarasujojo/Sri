a,b=input().split()
e=0
for i in range(int(a),int(b)+1):
    c=1
    d=0
    while c<=i:
        if i%c==0:
            d+=1
        c+=1
    if d==2:
        e+=1
print(e)
