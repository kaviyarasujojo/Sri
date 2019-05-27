import math
a,b=input().split()
c=math.gcd(int(a),int(b))
print((int(a)*int(b))//c)
