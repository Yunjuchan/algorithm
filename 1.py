def rotate(x, d) :
    if d == 1 :
        left[x] -= 1
        left[x] %= 8
        right[x] -= 1
        right[x] %= 8
    else :
        left[x] += 1
        left[x] %= 8
        right[x] += 1
        right[x] %= 8

cogs = [list(map(int, input())) for _ in range(4)]
N = int(input())
# 2번째 오른쪽 6번째 왼쪽
left = [6,6,6,6]
right = [2,2,2,2]

for i in range(N) :
    M, D = map(int, input().split())
    M -= 1
    rotate(M, D) 
    i = 0
    while M+i < 3 :
        
        if cogs[M+i][right[M+i]] != cogs[M+i+1][left[M+i+1]] :
            print(cogs[M+i][right[M+i]], cogs[M+i+1][left[M+i+1]])
            print([right[M+i]], [left[M+i+1]])
            rotate(M+i+1, D*(-1)**(i+1))
        else :
            break
        i += 1

    i = 0
    while M-i > 0 :
        if cogs[M-i][left[M-i]] != cogs[M-i-1][right[M-i-1]] :
            rotate(M-i-1, D*(-1)**(i+1))
        else :
            break
        i += 1



result = 0
for i in range(4) :
    result += cogs[i][(right[i]-2)%8] * (2**i)
print(result)

    


