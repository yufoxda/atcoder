n,l,r = map(int, input().split())

xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in xy:
    if(i[0] <= l and i[1] >= r):
        ans += 1
print(ans)