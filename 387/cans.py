def int_pow(a, t):
    return a ** t

def count(r):
    # r を数字のリストとして扱う
    digit = [int(d) for d in str(r)]
    n = len(digit)
    res = 0

    # r がヘビ数の場合
    #各桁に対して確認
    for i in range(1, n + 1):
        if i == n:
            res += 1
            break
        # 現在確認している桁より下の桁の組み合わせの数
        lownum = int_pow(digit[0], n - 1 - i)
        #　現在確認している桁で撮りうる値の数
        nownum = min(digit[0], digit[i])
        # 組み合わせの数を加算
        res += lownum * nownum
        
        if digit[i] >= digit[0]:
            break

    # 他の可能性を考慮
    for i in range(n):
        mx = (9 if i > 0 else digit[0] - 1)
        for j in range(1, mx + 1):
            res += int_pow(j, n - 1 - i)
    
    return res
'''
最初の部分では、5000 から 5928 までの範囲で、最上位桁（digit[0] = 5）を固定して、残りの桁の値を調べ、ヘビ数を数えています。
次の部分では、最上位桁が 5000 より小さい場合（0 から 4）の範囲で、残りの桁の組み合わせを数え、ヘビ数を数えています。
'''

def count_heavy_numbers(L, R):
    return count(R) - count(L - 1)

r,l = map(int, input().split())
print(count_heavy_numbers(r,l))
