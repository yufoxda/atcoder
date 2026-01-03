n, m = map(int, input().split())
s = input()
t = input()

min = 100000

if(t in s):
    print("0")
else:
    # 先頭から最後尾まで
    for i in range(0,n-m+1):
        tmp = s[i:i+m]
        tmp_count = 0
        # カウント
        # それぞれのけたに対し、
        for j in range(0,m):
            p = int(tmp[j])
            q = int(t[j])
            if(p < q):
                tmp_count += (9-q)+p+1
            else:
                tmp_count += p - q 
        # 最低値更新
        if tmp_count < min:
            min = tmp_count
    print(min)
