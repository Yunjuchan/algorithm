N = int(input())
i = 1
cnt = 0
total = 0
while total <= N :
    total += i
    i += 1
    cnt += 1
print(cnt-1)