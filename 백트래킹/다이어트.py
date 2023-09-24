N = int(input())
lst = []
condition = list(map(int, input().split()))
for _ in range(N) :
    lst.append(list(map(int, input().split())))
nutrient = [0,0,0,0,0]
def diet(level, start, nutrient, path) :
    global Min, Min_path
    tmp = 0
    for i in range(4) :
        if nutrient[i] >= condition[i] :
            tmp += 1
    if tmp == 4 :
        if Min > nutrient[4] :
            Min = nutrient[4]
            Min_path = path
        return
    
    if level == N :
        return
    
    for i in range(start, N) :
        new_nutrient = lst[i]
        for j in range(5) :
            new_nutrient[j] += nutrient[j]
        diet(level+1, i+1, new_nutrient, path+[i])
        for j in range(5) :
            new_nutrient[j] -= nutrient[j]
Min = 21e8
diet(0,0,[0,0,0,0,0], [])
if Min == 21e8 :
    print(-1)
else :
    print(Min)
    for i in Min_path :
        print(i+1, end=' ')