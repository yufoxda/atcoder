n = int(input())
l = list(map(int, input().split()))

tmp = 2
start = 0
for i in l:
    if i == 0:
        tmp += 1
        start += 1
    else:
        break

end = 0
for i in reversed(l):
    if (end + start) >= n:
        break
    if i == 0:
        tmp += 1
        end += 1
    else:
        break

ans = n + 1  - tmp


print(max(ans, 0))