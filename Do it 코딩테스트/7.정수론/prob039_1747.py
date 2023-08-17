n = int(input())
lst = [0] * 10000001
for i in range(2, 10000001) :
    lst[i] = i
for i in range(2, int(10000000 ** (1/2)) + 1) :
    if lst[i] == 0 :
        continue
    for j in range(2, 10000000 // i + 1) :
        lst[i*j] = 0
flag = 0
while n < 10000001 :
    if lst[n] != 0 :
        x = str(lst[n])
        i = 0 
        while True :
            if x[i] == x[-i-1] :
                i += 1
            else : break
            if i > len(x) // 2 :
                print(x)
                flag = 1
                break
    if flag == 1 :
        break
    n += 1
