N, K = map(int, input().split())
order_list = [[] for _ in range(101)]
cnt_list = [0] * (K+1)
lst = list(map(int, input().split()))
for i in range(K) :
    order_list[lst[i]].append(i)
multi = [-1] * N
result = 0
for i in range(K) :
    tmp = []
    flag = 0
    if lst[i] in multi :
        cnt_list[lst[i]] += 1
        continue

    for j in range(N) :
        if multi[j] == -1 :
            multi[j] = lst[i]
            cnt_list[lst[i]] += 1
            flag = 1
            break
        else :
            tmp.append(j)

    if flag == 1 :
        continue

    if tmp :
        next = i
        for x in tmp :
            idx = cnt_list[multi[x]]
            if idx >= len(order_list[multi[x]]) :
                Min_i = x 
                break
            if next < order_list[multi[x]][idx]:
                next = order_list[multi[x]][idx]
                Min_i = x


        multi[Min_i] = lst[i]
        cnt_list[lst[i]] += 1
        result += 1
 
print(result)
