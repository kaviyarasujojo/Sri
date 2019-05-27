import math
u,v=input().split()
q=math.gcd(int(u),int(v))
print((int(u)*int(v))//q)
