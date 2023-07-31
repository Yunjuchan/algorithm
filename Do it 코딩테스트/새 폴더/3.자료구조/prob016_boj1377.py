N = int(input())
flag = 0
lst = []
for i in range(N) :
    lst.append(int(input()))
try :
    for i in range(1,N+1) :
        flag = 0
        for j in range(1, N-i) :
            if lst[j-1] > lst[j] :
                flag = 1
                lst[j-1], lst[j] = lst[j], lst[j-1] 
        if flag == 0 :
            print(i)
            break
except :
    pass