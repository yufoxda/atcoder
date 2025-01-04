def round_up_to_highest_digit(input_number):
    # 数値の桁数を取得
    num_digits = len(str(input_number)) -1
    
    # 最高桁で繰り上げるための基準となる数値を求める
    rounded_number = 10 ** num_digits * (int(input_number[0]) + 1)
    
    return rounded_number

def round_down_to_highest_digit(input_number):
    # 数値の桁数を取得
    num_digits = len(str(input_number)) -1
    
    # 最高桁で繰り上げるための基準となる数値を求める
    rounded_number = 10 ** num_digits * (int(input_number[0]))
    
    return rounded_number




l,r=input().split()
a = len(l) - 1
print(round_up_to_highest_digit(l))
print(round_down_to_highest_digit(r))

aa = 0
for i in range(int(l[0]),int(r[0])+1):
    aa += (i-1)**(len(l)-1)
print(aa)


head = int(l[0])
bb =min(head -1,int(l[1]))
for i in l[2:]:
    bb *= min(head -1,int(i)) + 1
aa += bb
print(bb)
head = int(r[0])
cc = min(head -1,int(r[1]))
for i in r[2:]:
    cc *= min(head - 1,int(i)) + 1
print(cc)
aa += cc
print(aa)