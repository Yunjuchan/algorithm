N, C, W = map(int, input().split())
wood = []
length = 0
for _ in range(N) :
    x = int(input())
    wood.append(x)
    if x > length :
        length = x
Max = 0
while length >= 1 :
    cnt = 0
    cut = 0
    value = 0
    for x in wood :
        if x // length != 0 :
            cnt = x // length
            cut = x // length
            if x % length == 0 :
                cut -= 1
            if cnt * length * W - cut * C > 0 :
                value += cnt * length * W - cut * C
    if value > Max :
        Max = value 
    length -= 1

print(Max)

