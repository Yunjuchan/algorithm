import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N) :
    lst.append(list(map(int, input().split())))
lst.sort()
result = 0
A = [0] * 10001
for y, x1, x2 in lst :
    for i in range(x1, x2) :
        if i == x1 or i == x2-1:
            result += y - A[i] 
        A[i] = y 
print(result)
