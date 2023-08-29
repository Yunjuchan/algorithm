from collections import deque
import sys
input = sys.stdin.readline
bucket = list(map(int, input().split()))
lst = [0,0,bucket[2]]
direct = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]]
result = [lst[:]]
def pour(a, b, lst) :    # a양동이에서 b양동이로 물을 부어라
    total = lst[b]+ lst[a]
    if total >= bucket[b] :
        lst[b] = bucket[b]
        lst[a] = total - bucket[b]
    else :
        lst[b] = total
        lst[a] = 0
    return lst
def bfs() :
    que = deque()
    que.append(lst)
    while que :
        l = que.popleft()
        for i in range(6) :
            ret = pour(*direct[i], l[:])
            if ret not in result :
                result.append(ret)
                que.append(ret)
bfs()
x = set()
for res in result :
    if res[0] == 0 :
        x.add(res[2])
x = sorted(list(x))
print(*x)