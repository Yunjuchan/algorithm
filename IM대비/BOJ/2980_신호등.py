N, L = map(int, input().split())
lst = ['G'] * (L+1)
now = 0
sec = 0
traffic = []

def is_red(lst, sec) :
    if sec % (lst[1]+lst[2]) < lst[1] :
        return 'R'
    else :
        return 'G'
    
for _ in range(N) :
    traffic.append(list(map(int, input().split())))
while now != L :
    for t in traffic :
        lst[t[0]] = is_red(t, sec)
    if lst[now] == 'G' :
        now += 1
    sec += 1
print(sec)
