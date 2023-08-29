T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    mul = N*M
    while M != 0 :
        tmp = N % M
        N = M
        M = tmp
    print(mul // N)