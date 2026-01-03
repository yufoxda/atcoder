n, r = map(int, input().split())
l = list(map(int, input().split()))

# 元のコードの変数名を使用
left = -1
for i in range(n):
    if l[i] == 0:
        left = i
        break
right = -1
for i in range(n-1, -1, -1):
    if l[i] == 0:
        right = i
        break

# 開いているドアがない場合（元のロジックを改善）
if left == -1:  # sum(l) == n と同じ意味
    print(0)
    exit()

# 開いているドアの数
open_count = l.count(0)

# 元のコードの発想を改善: 
# 部屋Rから左側と右側に分けて考える
# 左側に移動するコスト + 右側に移動するコスト

# Rより左側の開いているドアの範囲
left_doors = [i for i in range(r) if l[i] == 0]
# Rより右側の開いているドアの範囲  
right_doors = [i for i in range(r, n) if l[i] == 0]

move_cost = 0

# 左側にドアがある場合、最も左まで移動して戻る
if left_doors:
    leftmost = min(left_doors)
    move_cost += 2 * (r - leftmost)

# 右側にドアがある場合、最も右まで移動して戻る
if right_doors:
    rightmost = max(right_doors)
    move_cost += 2 * (rightmost - r)

ans = open_count + move_cost
print(ans)