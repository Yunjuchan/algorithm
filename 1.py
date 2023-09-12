import sys
input = sys.stdin.readline
N, R1, C1, R2, C2 = map(int, input().split())

for i in range(R1, R2+1) :
    for j in range(C1, C2+1) :
        i %= (2*N-1)
        j %= (2*N-1)
        if i < N :
            if j < N-i-1 :
                print('.', end='')
            elif j < N+i :
                x = abs(N-1-j)
                n = (97+x+N-i-1-19) % 26 + 97
                print(chr(n), end='')
            else :
                print('.', end='')
    
        else :
            i -= N-1
            if j < i :
                print('.', end='')
            elif j < 2*N-i-1 :
                x = abs(N-1-j)
                n = (97+x+i-19) % 26 + 97
                print(chr(n), end='')
            else :
                print('.', end='')
            i += N-1
            
    print()
        
