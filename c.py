s = input()
n = len(s)

ans = 0
# まんなかまで計算
for i in range(n):
    # それぞれがかいしのとき
    for j in range(i+1,n+1,2):
        # j-1もじめまでをぬきだし
        l = j - i
        middle = int( (l + 1)/2)
        # print(s[i:j],middle,s[i+middle-1])
        if(s[i+middle-1] == 'C'):
            ans += 1

print(ans)






