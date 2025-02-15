s = input()
ans = 0
for j ,c in enumerate(s):
    n = 1
    while(j + n *2 < len(s)):
        if(s[j] == "A" and s[j+n] == "B" and s[j+n*2] == "C"):
            ans += 1
        n += 1
print(ans)