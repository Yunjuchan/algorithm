<<<<<<< HEAD
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
    
=======
# N = int(input())
# top = list(map(int, input().split()))
# A = [0]*N
# C = [1]*N
# for i in range(1,N) :
#     A[i] = A[top[i]]+C[top[i]]
#     C[top[i]] += 1

a = 13
b = 11
print(a&b)
>>>>>>> 658d5f71a5a702cfad4794b61a942fd11922a59f
