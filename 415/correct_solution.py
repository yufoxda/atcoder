def solve_medicine(n, s):
    """
    正しいアルゴリズム: DFSで安全な経路を探索
    """
    target = (1 << n) - 1  # 全ての薬品が混ざった状態
    
    def dfs(state):
        if state == target:
            return True
        
        # 各薬品を追加してみる
        for i in range(n):
            if not (state & (1 << i)):  # 薬品i+1がまだ混ざっていない
                new_state = state | (1 << i)
                # 新しい状態が安全かチェック (1-indexed)
                if new_state <= len(s) and s[new_state - 1] == '0':
                    if dfs(new_state):
                        return True
        
        return False
    
    return dfs(0)

# テスト
test_cases = [
    (3, "010"),
    (4, "1100"),
    (2, "11"),
    (3, "000"),
    (1, "0")
]

print("=== Correct algorithm results ===")
for n, s in test_cases:
    result = solve_medicine(n, s)
    print(f"n={n}, s='{s}': {'Yes' if result else 'No'}")

print("\n=== Original algorithm results ===")
def check_safe(s, now, n):
    if now == '':
        return True
    for i in range(n):
        if check_safe(s, now[1:], n-1):
            if s[int(now[0])] == '0':
                return True
    return False

for n, s in test_cases:
    result = check_safe(list(s), '0' * n, n)
    print(f"n={n}, s='{s}': {'Yes' if result else 'No'}")
