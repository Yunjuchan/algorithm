T = int(input())
for tc in range(1,T+1) :
    N = int(input()) 
    cnt = [0]*10
    i = 0
    while sum(cnt) < 10 :
        i += 1
        X = str(N*i)
        for j in X :
            cnt[int(j)] = 1
    print(f'#{tc} {N*i}')


        
