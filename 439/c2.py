n = int(input())

c = [0]*(n+1)

x = 1
while (x * x <= n):
    y = x + 1
    while (x * x + y * y <= n):
        c[x * x + y * y] += 1
        y += 1
    x += 1

ans = []
for i in range(n+1):
    if(c[i] == 1):
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)