def can_mix_all_medicines(n, safety):
    """
    全ての薬品を安全に混ぜることができるかを判定（C++版と同じアルゴリズム）
    
    Args:
        n: 薬品の種類数
        safety: 各状態の安全性を表す文字列（長さ2^n-1）
    
    Returns:
        bool: 全ての薬品を安全に混ぜることができるか
    """
    # C++版と同様に先頭に'0'を追加
    s = "0" + safety
    
    # 到達可能な状態をマークする配列
    ok = [False] * (1 << n)

    ok[0] = True  # 空の状態は到達可能
    
    # 各状態から次の状態への遷移を試行
    for i in range(1 << n):
        if not ok[i]:
            continue
        
        # 各薬品を追加してみる
        for j in range(n):
            if i & (1 << j):  # 薬品j+1が既に混ざっている場合はスキップ
                continue
            
            next_state = i | (1 << j)  # 薬品j+1を追加
            if s[next_state] == '0':   # 新しい状態が安全な場合
                ok[next_state] = True
    
    # 全ての薬品が混ざった状態に到達できるか
    return ok[(1 << n) - 1]


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if can_mix_all_medicines(n, s):
        print("Yes")
    else:
        print("No")




