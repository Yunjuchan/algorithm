N = input()
cnt = 0
tmp = 0
while len(N) != 1 :
    cnt += 1
    for i in N :
        tmp += int(i)
    N = str(tmp)
    tmp = 0
print(cnt)
if int(N) % 3 == 0 :
    print('YES')
else :
    print('NO')