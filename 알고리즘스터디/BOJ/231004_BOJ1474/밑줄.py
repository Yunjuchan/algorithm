import sys
N, M = map(int, input().split())
words = []
length = 0
for _ in range(N) :
    x = input().rstrip()
    length += len(x)
    words.append(x)
tmp = M - length
p, q = divmod(tmp, N-1)
result = words[0]
for i in range(1,N) :
    if q != 0 and 'a' <= words[i][0] <= 'z':
        result += '_'
        q -= 1
    elif N-i == q :
        result += '_'
        q -= 1
    result += '_'*p + words[i]
print(result)
