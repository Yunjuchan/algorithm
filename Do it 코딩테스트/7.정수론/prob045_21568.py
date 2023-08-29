A, B, C = map(int, input().split())
stack = []
while B != 0 :
    stack.append(A // B)
    tmp = A % B
    A = B
    B = tmp
x, y = 1, 0

if C % A == 0 :
    tmp = C // A
    while stack :
        q = stack.pop()
        x, y = y, x-y*q
    print(x*tmp, y*tmp)

else :
    print(-1)