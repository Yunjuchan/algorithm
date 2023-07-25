## 시간 초과 O(n^2)
# N = int(input())
# a = []
# i = 1
# while i <= N :
#     j = 1 
#     while j <= i :
#         if i % j == 0 :
#             a.append(j)
#         j += 1
#     i += 1
# print(sum(a))

## 시간 초과 O(n^(3/2))
# from math import sqrt
# N = int(input())
# a = []
# i = 1
# while i <= N :
#     j = 1 
#     while j <= sqrt(i) :
#         if i % j == 0 :
#             a.append(j)
#             if (i % j) == (i // j) :
#                 break
#             a.append(i // j)
#         j += 1
#     i += 1
# print(sum(a))

## 반복문을 1번만 써서 풀어보기
T = int(input())
total = 0
for i in range(1, T+1) :
    total += (T // i) * i
print(total)


# 문제 해결 x
## 좋은 접근 방식 계속 나머지를 구하는 것이 아니라 
# 나누어 떨어지는 개수를 구하고 나눈 값을 곱하는 방식으로 풀이


