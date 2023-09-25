N, M = map(int, input().split())
if N != 0 :
    lst = list(map(int, input().split()))
cnt = 0
i = 0
tmp = 0
while i < N :
    if M - tmp < lst[i] :
        tmp = 0
        cnt += 1
    else :
        tmp += lst[i]
        i += 1
if tmp != 0 :
    cnt += 1
print(cnt)