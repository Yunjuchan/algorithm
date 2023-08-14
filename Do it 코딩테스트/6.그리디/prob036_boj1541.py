from collections import deque
que = deque(input())
## 입력
tmp = 0
tmp2 = 0
flag = 1
result = 0
while que :
    # print(tmp2)
    x = que.popleft()
    if x.isdigit() :
        tmp = tmp*10 + int(x)
    elif x == '-' :
        result += flag * tmp
        tmp = 0
        flag = -1
    else :
        result += flag * tmp
        tmp = 0
result += flag * tmp
print(result)
    