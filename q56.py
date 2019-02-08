a=input()
b=False
c=False
d=[]
for i in a:
    try:
        if int(i)>=0 or int(i)<=0:
            d.append(i)
            continue
    except ValueError:
        f=True
    if(65<=ord(i)<=90 or 97<=ord(i)<=122):
        d.append(i)
        continue
for i in d:
     try:
        if int(i)>=0 or int(i)<=0:
            b=True
            continue
        else:
            b=False
     except ValueError:
         f=True
     if(65<=ord(i)<=90 or 97<=ord(i)<=122):
         c=True
         continue
     else:
         c=False
if (b==True and c==True):
    print("Yes")
else:
    print("No")
