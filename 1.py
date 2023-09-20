N = int(input())
lst = list(map(int, input().split()))
lst.sort()
Sum = 0
for i in range(N) :
    if Sum+1 >= lst[i] :
        Sum += lst[i]
        print(Sum)
    else :
        print(Sum+1)
        break
else :
    print(Sum + 1)