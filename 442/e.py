
import math



n,q = map(int, input().split())

enemy = []
for i in range(n):
    x,y = map(int, input().split())
    
    enemy.append([math.atan2(y, x),i])
tmp = enemy.copy()
enemy.sort(reverse=True)

hakai = []
anstmp = []
for _ in range(q):
    a,b = map(int, input().split())
    hakai.append([a,b])
    
    # enemyの2項目目がa-1またはb-1であるインデックスを取得
    idx_a = next(idx for idx, (angle, orig_idx) in enumerate(enemy) if orig_idx == a-1)
    idx_b = next(idx for idx, (angle, orig_idx) in enumerate(enemy) if orig_idx == b-1)
    anstmp.append([idx_a, idx_b])
print(enemy)
print(anstmp)
for i in range(q):
    ans = anstmp[i][1] - anstmp[i][0]
    print(ans)







