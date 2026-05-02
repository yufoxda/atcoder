A = []
for i in range(3):
    A.append(list(map(int, input().split())))

# 4 5 6
tmp = 1
tmp *= A[0].count(4) / 6
tmp *= A[1].count(5) / 6
tmp *= A[2].count(6) / 6


# 5 6 4
tmp2 = 1
tmp2 *= A[0].count(5) / 6
tmp2 *= A[1].count(6) / 6
tmp2 *= A[2].count(4) / 6

# 6 4 5
tmp3 = 1
tmp3 *= A[0].count(6) / 6
tmp3 *= A[1].count(4) / 6
tmp3 *= A[2].count(5) / 6

# 4 6 5
tmp4 = 1
tmp4 *= A[0].count(4) / 6
tmp4 *= A[1].count(6) / 6
tmp4 *= A[2].count(5) / 6

# 5 4 6
tmp5 = 1
tmp5 *= A[0].count(5) / 6
tmp5 *= A[1].count(4) / 6
tmp5 *= A[2].count(6) / 6

# 6 5 4
tmp6 = 1
tmp6 *= A[0].count(6) / 6
tmp6 *= A[1].count(5) / 6
tmp6 *= A[2].count(4) / 6

print((tmp + tmp2 + tmp3+ tmp4 + tmp5 + tmp6))