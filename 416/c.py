n, k, x = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

s.sort()

def base_n(num_10,n):
    if num_10 == 0:
        return '0'
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return (str_n[::-1])

astring = base_n(x, n)
# k桁になるように0埋め
astring = astring.zfill(k)
ans = ''
print(s)
if(astring[:-1]== '0'):
    astring = str(int(astring)-1)
print(astring)
for i in astring:
    ans += s[int(i)-1]

print(ans)
"""
nnnnnnnn
kとばし
x%(n*k) = aa
pritn n[aa]

k-1
x/(n*k)  

"""