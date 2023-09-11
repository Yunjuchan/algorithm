N, R1, C1, R2, C2 = map(int, input().split())
arr = []
for i in range(N) :
    lst = []
    for j in range(N-i-1) :
        lst.append('.')
    for j in range(N-i-1, N+i) :
        x = abs(N-1-j)
        lst.append(chr(97+x+N-i-1))
    for j in range(N+i, 2*N-1) :
        lst.append('.')
    arr.append(lst)    
    
'''
0일 때 N
1일때 N, N-1, N
2일 때 N, N-1, N-2, N-1, N

'''
for i in range(1, N) :
    lst = []
    for j in range(i) :
        lst.append('.')
    for j in range(i, 2*N-i-1) :
        x = abs(N-1-j)
        lst.append(chr(97+x+i))
    for j in range(2*N-i-1, 2*N-1) :
        lst.append('.')
    arr.append(lst)
        
for i in range(R1,R2+1) :
    for j in range(C1, C2) :
        print(arr[i%(2*N-1)][j%(2*N-1)], end='')
    print()
