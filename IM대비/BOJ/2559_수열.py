N, K = map(int, input().split())
lst = list(map(int, input().split()))
Max = tmp = sum(lst[:K])

start, end = 0, K-1
while end < N-1 :
    tmp -= lst[start]
    start += 1
    end += 1
    tmp += lst[end]
    if tmp > Max :
        Max = tmp
print(Max)