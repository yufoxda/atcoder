n = int(input())
a = list(map(int, input().split()))

# { 値、回数}
array = []

sakluzyo = 0

for i in range(0, n):


    if array and a[i] == array[-1][0]:
        array[-1][1] += 1

        if array[-1][1] == 4:
            array.pop()
            sakluzyo += 4

    else:
        array.append([a[i], 1])

print(n - sakluzyo)