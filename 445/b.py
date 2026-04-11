n = int(input())

s = []

max_len = 0
for i in range(n):
    tmp = input()
    if(len(tmp) > max_len):
        max_len = len(tmp)
    s.append(tmp)

for i in range(n):
    leni = len(s[i])
    tmp = ( max_len - leni ) // 2
    print("." * tmp + s[i] + "." * tmp)

