arr = list(range(1, 10001))
for num in arr :
    i = 1
    while True :
        tmp = num - i
        total = 0
        while tmp != 0 :
            total += tmp % 10
            tmp = tmp // 10
        if total == i :
            arr.remove(num)
        i += 1
print(arr)
        