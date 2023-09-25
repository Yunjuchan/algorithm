N, R, C  = map(int, input().split())
lst = []
while N :
    y = R // 2**(N-1)
    R %= 2**(N-1)
    x = C // 2**(N-1)
    C %= 2**(N-1)
    N -= 1
    lst.append([y, x])
result = 0
for i in lst :
    result = result * 4 + i[0]*2 + i[1]
print(result)