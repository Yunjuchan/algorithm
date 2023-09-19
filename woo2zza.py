import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = [0]*100
arr = [input().rstrip()*2 for _ in range(N)]
arr += arr

for i in range(2*N) :
    for j in range(2*M) :
        lst[ord(arr[i][j])] += i*j + (2*M-j)*(2*N-i) 
        lst[ord(arr[i][j])] += i*(2*M-j) + j*(2*N-i) 
        lst[ord(arr[i][j])] += N*M

for i in range(65, 92) :
    print(lst[i])
    