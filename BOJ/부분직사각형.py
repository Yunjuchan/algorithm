import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = [0]*100
arr = [input().rstrip()*2 for _ in range(N)]
arr += arr

for i in range(2*N) :
    for j in range(2*M) :
        lst[ord(arr[i][j])] += (2*M-j)*(j+1)*(2*N-i)*(i+1)

for i in range(65, 91) :
    print(lst[i])
    