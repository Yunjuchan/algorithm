def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    return ret

def union(w, a, b) :
    global result, cnt
    fa, fb = map(find, (a, b))
    if fa == fb :
        result += w
    else :
        cnt += 1
        top[fb] = fa
from heapq import heappush, heappop
N = int(input())
lan = [input() for _ in range(N)]
top = [-1] * N
result = 0
que = []
for i in range(N) :
    for j in range(N) :
        if 'a' <= lan[i][j] <= 'z' :
            tmp = ord(lan[i][j]) - 96
        elif 'A' <= lan[i][j] <= 'Z' :
            tmp = ord(lan[i][j]) - 38
        else : continue
        
        if i == j :
            result += tmp
            continue
        else :
            heappush(que, (tmp, i, j))
cnt = 0
while que :
    w, x, y = heappop(que)
    union(w, x, y)

if cnt == N-1 :
    print(result)
else :
    print(-1)

    