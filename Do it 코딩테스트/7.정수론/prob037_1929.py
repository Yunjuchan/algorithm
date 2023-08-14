M, N = map(int, input().split())
lst = [1] * (10**6+1)
lst[0] = lst[1] = 0
for i in range(2, int(N**(1/2))+1) :
    # if lst[i] == 0 :
    #     continue
    for j in range(2, N // i + 1) :
        lst[i*j] = 0
for i in range(M, N+1) :
    if lst[i] == 1 :
        print(i)
