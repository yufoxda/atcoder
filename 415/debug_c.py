def check_safe(s, now, n):
    print(f"check_safe called with s={s}, now='{now}', n={n}")
    if now == '':
        print("Base case: now is empty, returning True")
        return True
    
    for i in range(n):
        print(f"  Loop i={i}, checking recursion...")
        if check_safe(s, now[1:], n-1):
            print(f"  Recursion returned True, checking s[{int(now[0])}] == '0'")
            if s[int(now[0])] == '0':
                print(f"  s[{int(now[0])}] = '{s[int(now[0])]}' == '0', returning True")
                return True
            else:
                print(f"  s[{int(now[0])}] = '{s[int(now[0])]}' != '0'")
        else:
            print(f"  Recursion returned False")
    
    print("  No condition met, returning False")
    return False

# テストケース1つだけでデバッグ
print("=== Test case: n=3, s='010' ===")
s = ['0', '1', '0']
result = check_safe(s, '000', 3)
print(f"Final result: {result}")
