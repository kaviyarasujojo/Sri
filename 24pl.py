a=input()
b=0
for i in a:
    if 48<ord(i)<57:
        b+=1
if b==len(a):
    print("yes")
else:
    print("no")
