door = list(map(int, input()))
bucket = [0] * 10
cnt = 0
cnt_69 = 0

for i in range(len(door)):
    if door[i] == 6 or door[i] == 9 :
        cnt_69 += 1
    else :
        bucket[door[i]] += 1
        if bucket[door[i]] > cnt :
            cnt = bucket[door[i]]

set_69 = (cnt_69 + 1) // 2
if set_69 >= cnt :
    print(set_69)
else: print(cnt)