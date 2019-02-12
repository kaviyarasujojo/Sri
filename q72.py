a=input()
i=0
b=[]
for y in range(len(a)):
    if a[i].lower()=='a' or a[i].lower()=='e' or a[i].lower()=='i' or a[i].lower()=='o' or a[i].lower()=='u':
        b.append(a[i])
    else:
        i=i+1
if (len(b))>0:
    print("yes")
else:
    print("no")
