n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# 累積和を計算（D[i] = sum(A[0:i])）
D = [0] * (n + 1)
E = [0] * (n + 1)
F = [0] * (n + 1)

for i in range(n):
    D[i + 1] = D[i] + a[i]
    E[i + 1] = E[i] + b[i]
    F[i + 1] = F[i] + c[i]

# 最大化： D[x] - E[x] + E[y] - F[y] + F[N]
# 変形：   (D[x] - E[x]) + (E[y] - F[y]) + F[N]
#          = G[x] + H[y] + F[N]

# G[i] = D[i] - E[i]（i まで A を取る利得）
# H[j] = E[j] - F[j]（j まで B、その後 C を取る利得）
G = [D[i] - E[i] for i in range(n + 1)]
H = [E[i] - F[i] for i in range(n + 1)]

# y を全探索し、各 y について最適な x (< y) を累積maxで取得
# best_x = max(G[1], G[2], ..., G[y-1])
best_x = G[1]  # x の最小値は 1
ans = -(10**18)

for y in range(2, n):
    # 現在の y に対する最大値を計算
    ans = max(ans, best_x + H[y] + F[n])
    # 次の y のために best_x を更新
    best_x = max(best_x, G[y])

print(ans)