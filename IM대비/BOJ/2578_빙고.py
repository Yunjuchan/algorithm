from pprint import pprint
bingo_check = [0] * 12

bingo = [list(map(int,input().split())) for _ in range(5)] 
call = []
for i in range(5) :
    call += list(map(int, input().split()))
for i in range(25) :
    cnt = 0
    for y in range(5) :
        for x in range(5) :
            if bingo[y][x] == call[i] :
                bingo_check[y] += 1
                bingo_check[x+5] += 1
                if y == x :
                    bingo_check[10] += 1
                if (y + x) == 4 :
                    bingo_check[11] += 1
    for j in range(12) :
        if bingo_check[j] == 5 :
            cnt +=1
    if cnt > 2 :
        break
print(i+1) 
