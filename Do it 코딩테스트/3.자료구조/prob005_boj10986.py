# 나머지합 구하기
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
cnt_arr = [0] * M
tmp = 0
for i in arr :
    tmp += i 
    sum_arr.append(tmp)

# res_arr와 cnt_arr를 한번의 for문에 입력받았음
res_arr = list(map(lambda x : x % M, sum_arr))

for res in res_arr :
    cnt_arr[res] += 1
result = cnt_arr[0]

for cnt in cnt_arr :
    if cnt > 1 :
        result += cnt * (cnt-1) // 2

print(result)