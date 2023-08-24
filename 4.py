N = int(input())
result = -1
min_n = n = (N+2) // 3      ## 최소 갯수는 가장 작은 놈을 다 챙겨갔을 때보다 작아야함
for i in range(n) :
    cnt = i
    tmp = N - 5 * i   
    if tmp < 0 :
        break

    if tmp % 3 == 0 :
        cnt += tmp // 3
        if cnt <= min_n :
            min_n = cnt
            result = cnt
print(result)

