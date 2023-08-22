T = int(input())
for tc in range(1, T+1) :
    lst = list(map(int, input()))
    N = len(lst)
    claps = 0
    cnt = 0
    for i in range(N) :
        claps += lst[i]
        if claps <= i :
            cnt += 1
            claps += 1
    print(f'#{tc} {cnt}')
