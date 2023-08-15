N = int(input())
M = list(map(int, input()))
result = 0
S = len(M)
for i in range(S) :
    x = N * M[S-i-1]
    print(x)
    result += x * 10 ** i
print(result)