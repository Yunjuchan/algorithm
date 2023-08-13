import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
minus = []
plus = []
zero = 0
one = 0
result = 0
for _ in range(N) :
    x = int(input())
    if x < 0 :
        heappush(minus, x)
    elif x == 0 :
        zero += 1
    elif x == 1 :
        one += 1
    else :
        heappush(plus, -x)
# plus.sort()
# ## 음수쪽 처리
# while len(minus) > 1 :
#     x = heappop(minus)
#     y = heappop(minus)
#     result += x*y
# ## 양수쪽 처리
# while len(plus) > 1 :
#     x = plus.pop()
#     y = plus.pop()
#     result += x*y

# # 남은 값 처리
# if len(minus) == 1 :
#     if zero == 0 :
#         result -= minus[0]
# if len(plus) == 1 :
#     result += plus[0]
# result += one

# print(result)

## 음수쪽 처리
while len(minus) > 1 :
    x = heappop(minus)
    y = heappop(minus)
    result += x*y
## 양수쪽 처리
while len(plus) > 1 :
    x = heappop(plus)
    y = heappop(plus)
    result += x*y

# 남은 값 처리
if len(minus) == 1 :
    if zero == 0 :
        result += minus[0]
if len(plus) == 1 :
    result -= plus[0]
result += one

print(result)

