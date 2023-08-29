N, M = map(int, input().split())
while M != 0 :
    tmp = N % M
    N = M
    M = tmp
print('1'*N)