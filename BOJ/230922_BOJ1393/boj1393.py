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
d = 400
ret = gcd(dx, dy)
dx //= ret
dy //= ret

while True :
    if dx > 0 and x > 100 :
        break
    elif dx < 0 and x < -100 :
        break
    elif dy > 0 and y > 100 :
        break
    elif dy < 0 and y < -100 :
        break

    if d > (X-x)**2 + (Y-y)**2 :
        d = (X-x)**2 + (Y-y)**2
        r_x, r_y = x, y
    x += dx
    y += dy

print(r_x, r_y)