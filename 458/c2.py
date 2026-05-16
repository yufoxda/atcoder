s = input()
n = len(s)
ans = 0
for i in range(n):
    if(s[i] == "C"):
        ans += 1
        ans += min(i,n-i-1)
print(ans)