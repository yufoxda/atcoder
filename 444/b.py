n,k = map(int, input().split())

def cal(num):
    tmp = str(num)
    re = 0
    for i in range(len(tmp)):
        re += int(tmp[i])
    return re

ans = 0
for i in range(1,n+1):
    tmp = cal(i)
    if tmp == k:
        ans += 1
print(ans)