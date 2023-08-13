N, target = map(int, input().split())
stack = []
cnt = 0
for _ in range(N) :
    stack.append(int(input()))
while stack :
    print(target)
    x = stack.pop()
    cnt += target // x
    target -= (target // x) * x
    if target == 0 :
        break
print(cnt)