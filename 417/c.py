t = int(input())
test_cases = []

for i in range(t):
    a,b,c = map(int, input().split())
    test_cases.append((a,b,c))

for i in test_cases:
    a = i[0]
    b = i[1]
    c = i[2]
    min_val = min(a,b,c)

    if(not b == min_val):
        print(min_val)
    else:##ｂが最小値のとき
        #　残りの数
        a -= b
        c -= b
        ans = b
        if( a > c):
            pair = c
            if(pair > a-c):
                ans += a-c
            else:
                ans += pair
        elif(a < c):
            pair = a
            if(pair > c-a):
                ans += c-a
            else:
                ans += pair
        else:
            ans += (a+c)//3
        print(ans)
        