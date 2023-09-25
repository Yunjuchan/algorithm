X, Y = map(int, input().split())
x, y, dx, dy = map(int, input().split())
def gcd(a, b) :
    if abs(a) < abs(b) :
        a, b = b, a
    while b :
        tmp = a
        a = b
        b = tmp % b
    return a
d = (X-x)**2 + (Y-y)**2
if dx*dy != 0 :
    ret = gcd(dx, dy)
    dx //= abs(ret)
    dy //= abs(ret)
elif dx == 0 :
    dy //= abs(dy)
else :
    dx //= abs(dx)
    
r_x, r_y = x, y
while True :
    x += dx
    y += dy
    if d > (X-x)**2 + (Y-y)**2 :
        d = (X-x)**2 + (Y-y)**2
        r_x, r_y = x, y
    else :
        break

    if dx > 0 and x > 100 :
        break
    elif dx < 0 and x < -100 :
        break
    if dy > 0 and y > 100 :
        break
    elif dy < 0 and y < -100 :
        break

print(r_x, r_y)