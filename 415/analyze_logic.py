# 元のコードの動作を詳しく分析
def check_safe(s, now, n):
    print(f"check_safe(s, now='{now}', n={n})")
    if now == '':
        print("  Base case: empty string, return True")
        return True
    
    for i in range(n):
        print(f"  Loop i={i}")
        if check_safe(s, now[1:], n-1):
            print(f"    Recursive call returned True")
            print(f"    Checking s[{int(now[0])}] == '0': s[{int(now[0])}] = '{s[int(now[0])]}'")
            if s[int(now[0])] == '0':
                print(f"    s[{int(now[0])}] == '0', return True")
                return True
            print(f"    s[{int(now[0])}] != '0', continue loop")
        else:
            print(f"    Recursive call returned False")
    
    print("  No condition met, return False")
    return False

# テストケース2: n=4, s="1100"
print("=== Test case 2: n=4, s='1100' ===")
s = ['1', '1', '0', '0']
result = check_safe(s, '0000', 4)
print(f"Final result: {result}")
print()

# 状態の意味を確認
print("=== State meanings ===")
for i in range(1, 16):  # 1 to 15 (2^4 - 1)
    binary = format(i, '04b')
    medicines = [j+1 for j in range(4) if binary[3-j] == '1']
    print(f"State {i:2d}: binary={binary}, medicines={medicines}")
