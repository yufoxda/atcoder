n = input()

tmp = n[0]
for i in range(1, len(n)):
    if n[i] != tmp:
        print("No")
        exit()
print("Yes")