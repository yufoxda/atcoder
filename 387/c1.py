l, r = map(int, input().split())
n = 0  # 有効な数値のカウント
i = l  # 現在の値

while i <= r:
    s = str(i)
    head = int(s[0])  # 最初の桁
    is_valid = True

    # 各桁を確認
    for j in range(1, len(s)):
        if head <= int(s[j]):
            is_valid = False
            break

    if is_valid:
        n += 1
        i += 1  # 次の値を確認
    else:
        # 無効な値のスキップ
        for j in range(1, len(s)):
            if int(s[j]) >= head:  # スキップの基準
                # 次の候補値を計算
                i = int(s[:j]) * 10**(len(s) - j) + 10**(len(s) - j - 1)
                break
        else:
            # 全桁が不成立なら次の桁数へ
            i = 10**len(s)

print(n)
