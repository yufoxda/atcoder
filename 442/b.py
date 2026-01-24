q = int(input())
a = []
for i in range(q):
    a.append(int(input()))

vol = 0
ispalay = False

for i in a:
    if i == 1:
        vol += 1
    elif i == 2:
        vol = max(0, vol - 1)
    else:
        ispalay = not ispalay

    if ispalay and vol >= 3:
        print("Yes")
    else:
        print("No")