def is_palindrome(x, base):
    """数値xがbase進数で回文かどうかを判定"""
    if x == 0:
        return True
    
    digits = []
    temp = x
    while temp > 0:
        digits.append(temp % base)
        temp //= base
    
    # 回文チェック
    for i in range(len(digits)):
        if digits[i] != digits[len(digits) - 1 - i]:
            return False
    return True

def solve():
    a = int(input())
    n = int(input())
    
    base = 10
    vec = []  # 答えのリスト
    
    # powb[i] == 10**i
    powb = [1]
    length = 1
    
    while True:
        # powbを必要な分だけ拡張
        while len(powb) < length:
            w = powb[-1] * base
            powb.append(w)
        
        if powb[length - 1] > n:
            break
        
        # 上位半分の桁数
        half_len = (length + 1) // 2
        d = [0] * half_len  # 上位半分の桁
        d[0] = 1  # (1, 0, ..., 0) から開始
        
        while True:
            # dに対応するパリンドローム数を計算
            total = 0
            for i in range(length):
                if i < len(d):
                    idx = i
                else:
                    idx = (length - 1) - i
                total += powb[i] * d[idx]
            
            # (total <= n) かつ (totalがbase a で回文) かチェック
            if total <= n:
                if is_palindrome(total, a):
                    vec.append(total)
            
            # 次のd を生成
            has_next = False
            for i in range(len(d) - 1, -1, -1):
                if d[i] == base - 1:
                    d[i] = 0
                    continue
                else:
                    d[i] += 1
                    has_next = True
                    break
            
            if not has_next:
                break
        
        length += 1
    
    # 合計を計算
    result = sum(vec)
    print(result)

if __name__ == "__main__":
    solve()
