king, doll, N = input().split()
N = int(N)
k_x = ord(king[0]) - ord('A')
k_y = ord(king[1]) - ord('1')
d_x = ord(doll[0]) - ord('A')
d_y = ord(doll[1]) - ord('1')

direct_y = [0,0,-1,1,1,1,-1,-1]
direct_x = [1,-1,0,0,1,-1,1,-1]
def move(x, y, command) :
    if command == 'R' :
        dx = direct_x[0] + x
        dy = direct_y[0] + y
    elif command == 'L' :
        dx = direct_x[1] + x
        dy = direct_y[1] + y
    elif command == 'B' :
        dx = direct_x[2] + x
        dy = direct_y[2] + y
    elif command == 'T' :
        dx = direct_x[3] + x
        dy = direct_y[3] + y
    elif command == 'RT' :
        dx = direct_x[4] + x
        dy = direct_y[4] + y
    elif command == 'LT' :
        dx = direct_x[5] + x
        dy = direct_y[5] + y
    elif command == 'RB' :
        dx = direct_x[6] + x
        dy = direct_y[6] + y
    elif command == 'LB' :
        dx = direct_x[7] + x
        dy = direct_y[7] + y
    if 0 <= dy < 8 and 0 <= dx < 8 :
        return dx, dy
    return x, y    
for _ in range(N) :
    command = input()
    visited = [[False]*8 for _ in range(8)]
    last_k_x ,last_k_y = k_x, k_y
    last_d_x ,last_d_y = d_x, d_y
    k_x, k_y = move(k_x, k_y, command)
    if k_x == d_x and k_y == d_y :
        d_x, d_y = move(d_x, d_y, command)
        if last_d_x == d_x and last_d_y == d_y :
            k_x, k_y = last_k_x ,last_k_y 

print(chr(k_x+ord('A'))+chr(k_y+ord('1')))
print(chr(d_x+ord('A'))+chr(d_y+ord('1')))

