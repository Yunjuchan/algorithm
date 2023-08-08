N = int(input())
line = [0] * N
bucket = [1] * N
pick = list(map(int, input().split()))
for i in range(N) :
    x = i - pick[i]
    for j in range(N) :
        if line[j] >= x :
            line[j] += 1
    line[i] = x

for i in range(N) :
    bucket[line[i]] += i
print(*bucket)
