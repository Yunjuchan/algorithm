# import sys
# input = sys.stdin.readline
# N = int(input())
# cnt = 0
# lst = []
# for i in range(N) :
#     lst.append(int(input()))
# while True :
#     lst2 = []
#     cnt += 1
#     if len(lst) <= 1 :
#         break
#     for i in range(1,len(lst)) :
#         if lst[i-1] - lst[i] > 0 :
#             lst2.append(lst[i-1])
#     lst = lst2
        
# print(cnt)

import sys
input = sys.stdin.readline

N = int(input())
A = [(int(input()), i) for i in range(N)]
A.sort()

max_cnt = 0
for i in range(N) :
    cnt = A[i][1] - i
    if cnt > max_cnt :
        max_cnt = cnt
print(max_cnt + 1)