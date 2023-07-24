# 내코드 시간초과 오류
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = []
for i in range(N) :
    arr.append(list(map(int, input().split())))
# 내풀이 구간합 출력시 다시 for문 사용하니 시간초과가 발생함
# sum_arr = [[0] for i in range(N)]
# for i in range(N) :
#     tmp = 0
#     for j in range(N) :
#         tmp += arr[i][j]
#         sum_arr[i].append(tmp)

# for m in range(M) :
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     if x1 == x2 :
#         total = sum_arr[x2-1][y2] - sum_arr[x1-1][y1-1]
#     else :
#         for i in range(x1-1, x2) :
#             total += sum_arr[i][y2] - sum_arr[i][y1-1]

#     print(total)

# 구간합을 수식화 하여 설정한 뒤
sum_arr = [[0] * (N+1) for i in range(N+1)]
for i in range(1, N+1) :
    for j in range(1, N+1) :
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]

# 계산할때도 수식화하여 풀이
for m in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    total = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
    print(total)

## 구간합을 따로따로 구해서 시간 오류가 난 것