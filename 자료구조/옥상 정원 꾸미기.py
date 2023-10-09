import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
cnt = 0
result = 0
for i in range(N) :
    x = int(input().rstrip())
    while lst :
        if lst[-1] <= x :
            lst.pop()
            cnt -= 1
        else :
            lst.append(x)
            result += cnt
            cnt += 1
            break
    else :
        lst.append(x)
        cnt += 1
print(result)
    