a=input()
b=0
for i in a:
    try:
        if(int(i)>=0 or int(i)<=0):
            b+=1
    except ValueError:
        continue
print(b)
