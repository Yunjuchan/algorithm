N = int(input())
lst = list(map(int, input().split()))
start = 0
end = N-1
diff = 21e8
t1, t2 = None, None
while start < end :
    if abs(lst[start] + lst[end]) < diff :
        diff = abs(lst[start] + lst[end])
        t1 = lst[start]
        t2 = lst[end]
    if lst[start] + lst[end] > 0 :
        end -= 1
    elif lst[start] + lst[end] < 0 :
        start += 1
    else :
        break
print(t1, t2)