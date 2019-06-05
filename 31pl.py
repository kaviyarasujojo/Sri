a=input()
b=[]
for i in a:
    if i not in b:
        b.append(i)
if len(b)>1:
    if a.count(b[0])==a.count(b[1]):
        print("yes")
    else:
        print("no")
else:
    print("no")
