N, M = map(int, input().split())
cnt = 0
i = 1
while True :
    tmp = N // M ** i
    if tmp == 0 :
        break
    cnt += tmp
    i += 1
print(cnt)