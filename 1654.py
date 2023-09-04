N, M = map(int, input().split())
lst = []
start = 1
end = 0
for _ in range(N) :
    x = int(input())
    lst.append(x)
    if x > end :
        end = x
result = 0
while start <= end :
    cnt = 0
    mid = (start+end) // 2
    for i in lst :
        cnt += i // mid
    if cnt < M :
        end = mid - 1
    else :
        result = mid
        start = mid + 1
print(result)
    