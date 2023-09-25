L, R = input().split()
if len(R) != len(L) :
    print(0)
else :
    cnt = 0
    for i in range(len(R)) :
        if R[i] == L[i] == '8' :
            cnt += 1
        elif R[i] == L[i] != '8' :
                continue 
        else :
             break
    print(cnt)