n = int(input())
a = list(map(int, input().split()))

ans = [0] * n

# 後ろから計算
for i in range(n - 1, -1, -1):
    ans[i] = i + 1  # 1-indexed
    if ans[i] != a[i]:
        ans[i] = ans[a[i] - 1]  # 既に計算済みの結果を利用

print(*ans)

# for i in range(n):
#     tmp = a[i] - 1
#     time = 0
#     sumi = []

    # while True:
    #     # これを10^100回
    #     if(tmp in sumi and (not sumi)):
    #         break
    #     sumi.append(tmp)
    #     tmp = a[tmp] 
    #     time += 1
    #     print(sumi)
    # print(time,tmp,time-a.index(tmp))
    # time　- a.index(tmp) がループの長さ
    # (10^100 - a.index(tmp) ) % len(sumi) 
