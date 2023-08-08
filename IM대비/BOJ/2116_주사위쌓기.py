# # A, F // B, D // C, E
# # 쌓는 변수 생성
import sys
input = sys.stdin.readline
N = int(input())
dice_set = []
dice_pair = [5,3,4,1,2,0]

for i in range(N) :
    dice_set.append(list(map(int, input().split())))
max_side = 0

for i in range(6) :
    side = 6*N
    bottom = dice_set[0][i]
    top = dice_set[0][dice_pair[i]]
    
    if top + bottom == 11 :
        side -= 2
    elif top == 6 or bottom == 6 :
        side -= 1
    
    for i in range(1, N) :
        for j in range(6) :
            if dice_set[i][j] == top :
                bottom = dice_set[i][j]
                top = dice_set[i][dice_pair[j]]
                break
        if top + bottom == 11 :
            side -= 2
        elif top == 6 or bottom == 6 :
            side -= 1         
    if side > max_side :
         max_side = side
    
print(max_side) 
