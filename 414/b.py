n = int(input())
c=[]
l = []
for i in range(n):
    c_i, l_i = map(str, input().split())
    c.append(c_i)
    l.append(int(l_i))

if(sum(l)> 100):
    print("Too Long")
    exit()

for i in range(n):
    for j in range(l[i]):
        print(c[i], end="")

print()