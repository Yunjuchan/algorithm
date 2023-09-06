N = int(input())
lst = []
for _ in range(N) :
    lst.append(input())    
lst = sorted(lst, key=lambda x : (len(x), lst.count(x)))
cnt = 0
for i in range(N) :
    l = len(lst[i])
    for j in range(i+1, N) :
        if lst[j][:l] == lst[i] :
            cnt += 1
            break
print(N-cnt)