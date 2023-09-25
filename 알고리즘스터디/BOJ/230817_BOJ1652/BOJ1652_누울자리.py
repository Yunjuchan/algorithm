N = int(input())
arr = [input() for _ in range(N)]
arr_t = list(zip(*arr))

for i in range(N) :
    arr[i] = arr[i].split('X')

cnt_x = cnt_y = 0
for i in range(N) :
    arr_t[i] = ''.join(list(arr_t[i]))

for i in range(N) :
    arr_t[i] = arr_t[i].split('X')

for i in range(N) :
    for j in arr[i] :
        if len(j) >= 2 :
            cnt_x += 1
    for j in arr_t[i] :
        if len(j) >= 2 :
            cnt_y += 1
print(cnt_x, cnt_y)