n = int(input())
a = list(map(int, input().split()))
a = [i-1 for i in a]
ans = []
aaaaaa = 10**100


for i in range(n):
    tmp = a[i]
    time = 0
    sumi = set()
    if(a[i] == i):
        ans.append(a[i] + 1)
        continue
    while time <= n:
        if(tmp in sumi):
            break
        sumi.add(tmp)
        tmp = a[tmp]
        time += 1
    # tmp: ループの開始点
    # time: ループが始まるまでの時間
    # len(sumi)　- time: ループの長さ
    # (aaaaaa - time) % (len(sumi) - time) : ループの開始点から、aaaaaaまでの時間をループの長さで割った余り

    if( len(sumi) - time > 0):
        for i in range((aaaaaa - time) % (len(sumi) - time)):
            tmp = a[tmp]

    ans.append(a[tmp] +1)

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
