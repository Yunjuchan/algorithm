num = list(map(int, input()))
bucket = [0] * 10

set_buck = bucket[0]
cnt_69 = 0

for i in range(len(num)):
    if num[i] == 6 or num[i] == 9 :
        cnt_69 += 1
    else :
        bucket[num[i]] += 1
for i in range(len(bucket)):
    if bucket[i] > set_buck:
        set_buck = bucket[i]

set_69 = (cnt_69 + 1) // 2

if set_69 >= set_buck:
    print(set_69)
else: print(set_buck)