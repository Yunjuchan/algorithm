# 내풀이 속도 244ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]   # 0번째부터 합 구하기 위해 sum[i] = sum[i-1] + arr[i]
for i in range(N) :
    sum_arr.append(sum_arr[i] + arr[i])
for j in range(M) :
    start, end = map(int, input().split())
    print(sum_arr[end] - sum_arr[start-1])

# 책풀이 속도 248ms
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]   # 아무것도 더하지 않았을때를 위해 0을 넣어서 초기화
temp = 0 # 첫번째부터의 합 변수
for a in arr :
    temp += a
    sum_arr.append(temp)
for i in range(M) :
    s, e = map(int, input().split())
    print(sum_arr[e] - sum_arr[s-1]) # 뺄때는 s-1로 해주어야 s부터 더해짐

