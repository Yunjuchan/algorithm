# pypy로 실행 성공
N = int(input())
area = [0] * (N+1)
arr = [[0]*1001 for _ in range(1001)]
def draw(x, y, a, b, n) :
    for i in range(b) :
        for j in range(a) :
            arr[y+i][x+j] = n
for i in range(1,N+1) :
    y, x, a, b = map(int, input().split())
    draw(y, x, a, b, i)
for y in range(1001) :
    for x in range(1001) :
        area[arr[y][x]] += 1
print(*area[1:], sep='\n')