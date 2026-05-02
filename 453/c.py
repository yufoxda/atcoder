n = int(input())
l = list(map(int, input().split()))

ll = [x * 2 for x in l]


ans = 0
for mask in range(1 << n):
    cnt = 0
    now = 1

    for i in range(n):
        prev = now
        if (mask >> i) & 1:
            now += ll[i]
        else:
            now -= ll[i]

        if prev * now < 0:
            cnt += 1

        if cnt + (n - i - 1) <= ans:
            cnt = 0
            break

    if cnt > ans:
        ans = cnt

print(ans)