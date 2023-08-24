N, M = map(int, input().split())
A = [i for i in range(10 ** N+1)]
A[0] = A[1] = 0
for i in range(2, 10**N+1) :
    for j in range(i, 10**N//i+1) :
        A[i*j] = 0
print(A)
lst1 = []
cnt = 0
## 순열 필요
visited = [False] * 10
def abc(level, tmp) :
    if level == N :
        tmp2 = tmp
        while tmp2 % M == 0 :
            tmp2 //= M
        for j in range(2, int(tmp2**(1/2))+1) :
            if tmp2 % j == 0 :
                if A[j] == j and A[tmp2//j] == tmp2//j :
                        lst1.append(tmp)
        return
    for i in range(10) :
        if level == 0 and i == 0 :
            continue
        if not visited[i] :
        
            visited[i] = True
            abc(level+1, tmp*10+i)
            visited[i] = False
abc(0,0)
for i in lst1 :
    for j in range(2, i//2+1) :
        if j == 2 and i % 2 == 0:
            continue
        elif j != 2 and i % 2 == 1 :
            continue
        if A[i-j] == i-j and A[j] == j and i != 2*j:
            cnt += 1
            break
print(cnt)