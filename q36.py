a=input()
c=[]
b=0
for i in a:
     try:
         if int(i)>=0:
            continue
     except ValueError:
         c.append(i)
for i in c:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        continue
    else:
        b+=1
print(b)
