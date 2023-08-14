# ## 메모리 초과
# N, M = map(int, input().split())
# lst = [1] * (M+1)
# lst[0] = lst[1] = 0
# cnt = 0
# for i in range(2, int(M**(1/2)+1)) :
#     if lst[i] == 0 :
#         continue
#     for j in range(2, M // i + 1) :
#         lst[i*j] = 0

# for i in range(2, M+1) :
#     if lst[i] == 1 :
#         j = 2
#         while i ** j <= M :        
#             if N <= (i ** j) <= M :
#                 cnt += 1
#             j += 1 
# print(cnt)


## 메모리 초과
N, M = map(int, input().split())
lst = [1] * (M+1)
lst[0] = lst[1] = 0
cnt = 0
for i in range(2, int(M**(1/2)+1)) :
    if lst[i] == 0 :
        continue
    for j in range(2, M // i + 1) :
        lst[i*j] = 0

for i in range(2, M+1) :
    if lst[i] == 1 :
        for j in range(2, 48) :
            if N <= i ** j <= M :
                cnt += 1
            elif i ** j > M :
                break

print(cnt)


