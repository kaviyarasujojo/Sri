a=int(input())
b=input()
c=''
for i in range(-1,-a-1,-1):
    if b[i].lower() not in "aeiou":
        c+=b[i]
print(c)
