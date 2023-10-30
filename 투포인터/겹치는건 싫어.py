N, K = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
j = 1
result = 1
Max = 0
H = [0] * 100001
H[arr[i]] = 1
while j < N :
    # arr[j]의 개수가 K와 같으면 j번째 숫자는 수열에 들어올 수 없음
    if i == j :
        H[arr[j]] += 1
        j += 1
        continue

    if H[arr[j]] >= K :
        if Max < j-i :
            Max = j-i
        H[arr[i]] -= 1
        i += 1
        
    else :
        H[arr[j]] += 1
        j += 1
        
if Max < j-i :
    Max = j-i
print(Max)