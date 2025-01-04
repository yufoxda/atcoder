import collections
import math
n,k = map(int,input().split())
s = list(input())
c = collections.Counter(s)
all = math.factorial(n)
for i in list(c.values()):
    all /= math.factorial(i)
moinus = 0
if(k%2 == 0):
    gu=0
    
    for i in (c.values()):
        if(i >= 2):
            gu += i//2
    moinus = math.comb(gu, k//2)*2
else:
    ki = 0
    gu = 0
    
    for i in (c.values()):
        if(i >= 2):
            gu += i//2
            ki += i%2
            
        else:
            ki += i

    moinus = math.comb(gu, (k-1)//2)*ki*2*math.factorial(gu)+ math.comb(gu-1,(k-1)//2)*(ki+2)*2
print(int(all - moinus))
