import time

N, M = map(int, input().split())
def bridge(n, m) :
    arr= [[0 for i in range(N)] for j in range(M)]
    total = 0
    if n == 1:
        return m
    for i in range(1, m-n+2) :
        total += bridge(n-1, m-i)
    return total
start1 = time.time()       
result1, cnt1 = bridge(N, M)
end1 = time.time()
print(f'재귀 실행시간 : {end1 - start1} 재귀 값 : {result1}')

N, M = map(int, input().split())
arr = [[0 for j in range(M)] for i in range(N)]
start2 = time.time()
for i in range(N) :
    for j in range(M) :
        if i == 0 :
            arr[i][j] = j + 1
        elif i <= j:
            arr[i][j] = sum(arr[i-1][:j])
result2 = arr[N-1][M-1]
end2 = time.time()
print(f'동적계획 실행시간 : {end2 - start2} 동적계획 값 : {result2}')

## 백준 제출 코드

# T = int(input())
# for t in range(T) :
#     N, M = map(int, input().split())
#     arr = [[0 for j in range(M)] for i in range(N)]

#     for i in range(N) :
#         for j in range(M) :
#             if i == 0 :
#                 arr[i][j] = j + 1
#             elif i <= j:
#                 arr[i][j] = sum(arr[i-1][:j])
#     print(arr[N-1][M-1])



