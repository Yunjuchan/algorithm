N, M = map(int, input().split())
lst = list(map(int, input().split()))
value = lst[0]
s = e = 0
Min = 21e8
while True :
    if value >= M :
        if e - s + 1 < Min :
            Min = e - s + 1
        value -= lst[s]
        s += 1
    else :
        e += 1
        if e == N :
            break
        value += lst[e]
    
    if s > e :
        e += 1
        if e == N :
            break
        value += lst[e]    
    
    
if Min == 21e8 :
    print(0)
else : 
    print(Min)