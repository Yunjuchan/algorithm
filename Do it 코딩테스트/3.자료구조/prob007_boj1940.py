# 투포인터
N = int(input())
M = int(input())
materials = list(map(int, input().split()))
materials.sort()
idx1 = 0
idx2 = N-1
cnt = 0
while idx1 < idx2 :
    if materials[idx1] + materials[idx2] > M :
        idx2 -= 1
    elif materials[idx1] + materials[idx2] == M:
        cnt += 1
        idx1 += 1
        idx2 -= 1
    else :
        idx1 += 1
print(cnt)