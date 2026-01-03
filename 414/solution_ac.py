def even_mirror(n):
    """偶数桁パリンドロームを生成 (例: 123 -> 123321)"""
    s = str(n)
    new_n = int(s + s[::-1])
    return new_n

def odd_mirror(n, mid):
    """奇数桁パリンドロームを生成 (例: 123, 4 -> 1234321)"""
    s = str(n)
    new_n = int(s + str(mid) + s[::-1])
    return new_n

def convert(n, b):
    """10進数nをb進数文字列に変換"""
    if n == 0:
        return "0"
    ans = []
    while n > 0:
        ans.append(n % b)
        n //= b
    return "".join(map(str, reversed(ans)))

def is_kaibun(s):
    """文字列が回文かどうか判定"""
    return s == s[::-1]

def main():
    a = int(input())
    n = int(input())
    d = len(str(n))  # nの桁数
    total = 0
    
    # パリンドローム生成の上限を効率的に設定
    temp = int("9" * (d // 2)) if d // 2 >= 1 else 1
    
    # 1桁の数字をチェック (1-9, 0は除く)
    for i in range(1, min(10, n + 1)):
        if is_kaibun(convert(i, a)):
            total += i
    
    # 0も追加でチェック (nが0以上の場合)
    if n >= 0 and is_kaibun(convert(0, a)):
        total += 0
    
    # 2桁以上のパリンドロームを生成
    for i in range(1, temp + 1):
        # 偶数桁パリンドローム
        even = even_mirror(i)
        if even <= n and is_kaibun(convert(even, a)):
            total += even
        
        # 奇数桁パリンドローム生成の桁数制限チェック
        if len(str(i)) * 2 + 1 > d:
            continue
            
        # 奇数桁パリンドローム (中央桁0-9)
        for mid in range(10):
            odd = odd_mirror(i, mid)
            if odd <= n and is_kaibun(convert(odd, a)):
                total += odd
    
    print(total)

if __name__ == "__main__":
    main()
