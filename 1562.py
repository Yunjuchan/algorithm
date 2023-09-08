import sys
input = sys.stdin.readline
N = int(input())
X = []
Y = []
for i in range(N) :
    x, y = map(int, input().split()) 
    X.append(x)
    Y.append(y)
result = 0
for i in range(-1, N-1) :
    result += (X[i] * Y[i+1] - X[i+1] * Y[i])

print(abs(result/2))