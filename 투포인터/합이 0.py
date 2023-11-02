N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(N-2) :
    tmp1 = arr[i]
    a = i+1
    b = N-1
    while a < b :
        tmp2 = arr[a] + arr[b]
        if tmp1 + tmp2 > 0 :
            b -= 1
        elif tmp1 + tmp2 < 0 :
            a += 1
        else :
            if arr[a] == arr[b] :
                cnt += (b-a) * (b-a+1) // 2
                break
            else :
                x = y = 1
                while arr[a] == arr[a+1] :
                    x += 1
                    a += 1
                while arr[b] == arr[b-1] :
                    y += 1
                    b -= 1
                cnt += x*y
                a += 1
                

print(cnt)