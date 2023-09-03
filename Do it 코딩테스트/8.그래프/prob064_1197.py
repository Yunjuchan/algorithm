def find(x) :
    if top[x] == 0 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret
def union(a, b, w) :
    fa, fb = map(find, [a, b])
    global total
    if fa == fb :
        return
    else :
        total += w
        top[fb] = fa
N, M = map(int, input().split())
top = [0] * (N+1)
edge = []
total = 0
for _ in range(M) :
    edge.append(list(map(int, input().split())))
edge.sort(key=lambda x : x[2])
for s, e, w in edge :
    union(s, e, w)
print(total)