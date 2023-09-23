N = int(input())
stack = [[int(input()), 1]]
n = 1   # 스택의 길이
result = 0
for _ in range(N-1) :
    x = int(input())
    while stack :
        if stack[-1][0] < x :
            result += stack[-1][1]
            stack.pop()
            n -= 1
        elif stack[-1][0] == x : 
            result += stack[-1][1]
            stack[-1][1] += 1
            if n != 1 :
                result += 1
            break
        else :
            result += 1
            stack.append([x,1])
            n += 1
            break
    else :
        stack.append([x, 1])
        n += 1
print(result)