
## 메모리 초과
# N = 15
# lst = list(range(N+1))
# start = end = 1
# cnt = 0
# while start <= N :
#     if sum(lst[start:end+1]) > N :
#         start += 1
#         end = start
#     elif sum(lst[start:end+1]) == N :
#         cnt += 1  
#         start += 1
#         end = start 
#     else :
#         end += 1
# print(cnt)


## 시간 초과
# N = int(input())
# start = end = 1
# cnt = 0
# total = 0
# while start <= N :
#     total = ((start + end) * (end - start + 1)) // 2
#     if total > N :
#         start += 1
#         end = start
#     elif total == N :
#         cnt += 1  
#         start += 1
#         end = start 
#     else :
#         end += 1
# print(cnt)

# 토탈을 따로 계산하는게 시간초과가 나왔음
N = int(input())
start = end = 1
cnt = 1
total = 1
while end != N :
    if total > N :
        total -= start
        start += 1
    elif total == N :
        cnt += 1  
        total -= start
        start += 1
    else :
        end += 1
        total += end
print(cnt)

## 책에서 풀이
N = int(input())
start = end = 1
cnt = 1
total = 1
while end != N :
    if total > N :
        total -= start
        start += 1
    elif total == N :
        cnt += 1  
        end += 1
        total += end
    else :
        end += 1
        total += end
print(cnt)