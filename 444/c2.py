n = int(input())
a = list(map(int, input().split())) 

a.sort()
ans = []

if n % 2 == 1:
    # 奇数
    # この中にLがある
    # なかったら割れているはずなのにペアがいなくなる。->矛盾

    # あるとしたらこれの最大値
    kari = a[-1]
    
    nokori = [i for i in a if i != kari]
    #chekku
    if nokori and len(nokori) % 2 == 0:
        #　すべてにペアがいる必要がある
        flag = True
        for i in range(0, len(nokori)//2):
            if nokori[i] + nokori[-i-1] != kari:
                flag = False
                break
        if flag:
            # ok
            ans.append(kari)
    elif not nokori:
        # すべてが同じ長さ（分かれていない）ときのみ
        ans.append(kari)
                
else:
    # 偶数
    # この中に割れていないものがあるかもないかもしれない
    kari = a[-1]
    nokori = [i for i in a if i != kari]

    if nokori and len(nokori) % 2 == 0:
        # 割れていないものがある
        flag = True
        for i in range(0, len(nokori)//2):
            if nokori[i] + nokori[-i-1] != kari:
                flag = False
                break
        if flag:
            # ok
            ans.append(kari)
    elif not nokori:
        # すべてが同じ値（分かれていない）場合
        ans.append(kari)
    
    flag = True
    for i in range(0, len(a)//2):
        if a[i] + a[-i-1] != a[-1] + a[0]:
            flag = False
            break
    if flag:
        # ok
        ans.append(a[0] + a[-1])
print(*sorted(ans))

