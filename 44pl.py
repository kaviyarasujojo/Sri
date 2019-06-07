a,b=input().split()
c=a[-int(b):]
d=a[:len(a)-len(c)]
print(c+d)
