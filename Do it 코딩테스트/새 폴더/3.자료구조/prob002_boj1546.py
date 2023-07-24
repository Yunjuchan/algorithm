# 내풀이
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for i in range(N) :
    scores[i] = scores[i] / M * 100
print(sum(scores) / N)

# 책풀이
N = int(input())
mylist = list(map(int, input().split()))
M = max(mylist)
print(sum(mylist) / M / N * 100)