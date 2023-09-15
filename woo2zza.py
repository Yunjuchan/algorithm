N = int(input())
score = [0] * N
lst = list(map(int, input().split()))
for i in range(N) :
    for j in range(i+1, N) :
        if lst[i] % lst[j] == 0 :
            score[i] -= 1
            score[j] += 1
        if lst[j] % lst[i] == 0 :
            score[j] -= 1
            score[i] += 1
print(*score)