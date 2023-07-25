# import sys
# input = sys.stdin.readline
# T = int(input())
# for t in range(T) :
#     N = int(input())
#     total = 0
#     for i in range(1, N+1) :
#         total += (N // i) * i
#     print(total)

T = 9
total = [0] * (T+1)
for i in range(1, T+1) :
    total[i] = (T // i) * i + total[i-1]
print(total)