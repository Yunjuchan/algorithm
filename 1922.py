def find(x) :
    if top[x] == 0 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret

def union(a, b, c) :
    global total
    fa, fb = map(find, [a, b])
    if fa == fb :
        return
    total += c
    top[fb] = fa

N = int(input())
M = int(input())
top = [0] * (N+1)
adj = []
for _ in range(M) :
    adj.append(list(map(int, input().split())))
adj.sort(key=lambda x : x[2])
total = 0
for s, e, w in adj :
    union(s, e, w)
print(total)