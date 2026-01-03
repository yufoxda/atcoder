n = input()
sumi = []

mada = True

list = [0,1,4,9,16,25,36,49,64,81]
while mada:
    tugi = 0
    for i in range(len(n)):
        
        tugi += list[int(n[i])]
    if(tugi == 1):
        print("Yes")
        exit()
    
    if(tugi in sumi):
        print("No")
        exit()
    sumi.append(tugi)
    
    n = str(tugi)