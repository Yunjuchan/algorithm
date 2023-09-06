N = int(input())
lst = list(map(int, input().split()))
lst.sort()
start = 0
end = N-1
mid = 1
diff = 31e8
t1, t2, t3 = None, None, None
while mid < end and start < mid :
    if abs(lst[start] + lst[mid] + lst[end]) < diff :
        diff = abs(lst[start] + lst[mid] + lst[end])
        t1 = lst[start]
        t2 = lst[mid]
        t3 = lst[end]

    if lst[start] + lst[mid] + lst[end] > 0 :
        end -= 1
        if mid == end :
            mid -= 1
    elif lst[start] + lst[mid] + lst[end] < 0 :
        if end - mid == 1 :
            start += 1
            mid = start+1
            end = N-1
        else :
            mid += 1
    else :
        break

print(t1, t2, t3)