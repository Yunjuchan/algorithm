X = int(input())
length = 0
piece = 64
cnt = 0
while X != length :
    if X >= length + piece :
        length += piece
        cnt += 1
    piece = piece // 2
print(cnt)

# 단순히 조건대로 작성